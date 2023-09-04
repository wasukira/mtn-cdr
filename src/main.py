import logging
import sys
import os
import time
from typing import List
import argparse
from datetime import timedelta, datetime
from sqlalchemy import engine, text
from sqlalchemy.orm import sessionmaker
from model.cs5_ccn_voice_ma import Cs5CcNVoiceMA, TABLE_HEADERS
import pandas as pd
from utils.utils import Utils
from utils.queries import ccn_voice_sql_stmt, pg_ccn_voice_sql_stmt

os.environ['PATH'] += os.pathsep + "C:\\Users\\USER\\Desktop\\instantclient_19_20"

logging.basicConfig(format='[%(asctime)s] - [%(levelname)-8s] - [%(module)s:%(lineno)d ] - %(message)s',
                    datefmt='%Y-%m-%d:%H:%M:%S',

                    level=logging.INFO,
                    stream=sys.stdout)

logger = logging.getLogger("main")

FILE_RECORD_COUNT: int = 3000
FILE_SEQUENCE_LENGTH: int = 5

HEADERS = False

POSTGRES_DIALECT = True

parser = argparse.ArgumentParser()
parser.add_argument("table_name", help="Name of the table")
parser.add_argument("start_date", help="Start Date")
parser.add_argument("end_date", help="End Date")

args = parser.parse_args()
table_name = args.table_name
start_date = args.start_date
end_date = args.end_date

if POSTGRES_DIALECT:
    db_host = 'localhost'
    db_user = 'airflow'
    db_pass = 'airflow'
    db_name = 'airflow'
    db_port = 5435
    engine = engine.create_engine(f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}")
else:
    DIALECT = 'oracle'
    SQL_DRIVER = 'cx_oracle'
    USERNAME = 'DATA_EXTRACT_GDE'  # enter your username
    PASSWORD = 'DATA_EXTRACT_GDE'  # enter your password
    HOST = '10.156.209.95'  # enter the oracle db host url
    PORT = 1521  # enter the oracle port number
    SERVICE = 'BIBRST'  # enter the oracle db service name
    ENGINE_PATH_WIN_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD + '@' + HOST + ':' + str(PORT) + '/?service_name=' + SERVICE

    engine = engine.create_engine(ENGINE_PATH_WIN_AUTH)

factory = sessionmaker(bind=engine)
session = factory()

streaming_strategy = True

# table -> schema_prefix
tables_schema_mapping = {
    'CS5_AIR_REFILL_MA': {
        'schema_prefix': 'STG_CDR',
        'date_str': 'MONTH_YEAR'
    },
    'CS5_CCN_GPRS_MA': {
        'schema_prefix': 'STG_CDR',
        'date_str': 'MONTH_YEAR'
    },
    'CS5_CCN_SMS_MA': {
        'schema_prefix': 'STG_CDR',
        'date_str': 'MONTH_YEAR'
    },
    'CS5_CCN_VOICE_MA': {
        'schema_prefix': 'STG_CDR',
        'date_str': 'MONTH_YEAR',
        'obj': Cs5CcNVoiceMA,
        'sql': pg_ccn_voice_sql_stmt,
        'order_by': 'CALL_TIME',
        'path': os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'dumps', 'ccn_voice'),
        'file_name': "voice_cdr_"
    },
    'CS5_CCN_WMX_MA': {
        'schema_prefix': 'STG_CDR',
        'date_str': 'MONTH_YEAR'
    },
    'CS5_SDP_ACC_ADJ_MA': {
        'schema_prefix': 'STG_CDR',
        'date_str': 'MONTH_YEAR'
    },
    'CS5_SDP_DUMP_DA': {
        'schema_prefix': 'STG_CDR',
        'date_str': 'MONTH_YEAR'
    },
    'FCT_CDR_RECHARGE': {
        'schema_prefix': 'CDR_RECHARGE',
        'date_str': 'YEARMONTH'
    }, 'CS5_SDP_DUMP_UT': {
        'schema_prefix': 'STG_CDR',
        'date_str': 'MONTH_YEAR'
    }, 'CS5_SDP_DUMP_UC': {
        'schema_prefix': 'STG_CDR',
        'date_str': 'MONTH_YEAR'
    },
    'FCT_CDR_UNRATED': {
        'schema_prefix': 'STG_CDR',
        'date_str': 'MONTH_YEAR'
    },
}


def persist_record(batch, file_path, file_name):
    df = pd.DataFrame(batch)
    os.makedirs(file_path, exist_ok=True)
    full_file_name = os.path.join(file_path, file_name)
    df.to_csv(full_file_name, sep=',', encoding='utf-8', index=False, header=False)


def process_cdr(table_definitions, schema: str, schema_table_name, table_partitions):
    for table_partition in table_partitions:

        logger.info(f"started processing partition {schema} - {table_partition}")
        start_time = time.time()

        if POSTGRES_DIALECT:
            sql = f"{table_definitions['sql']} ccn_voice"
        else:
            sql = f"{table_definitions['sql']} {schema}.{schema_table_name} PARTITION (P_{table_partition})"

        # logger.info(sql)

        if streaming_strategy:
            query = text(sql)
            proxy = engine.execution_options(stream_results=True).execute(query)
            file_sequence = 0
            while True:
                batch = proxy.fetchmany(FILE_RECORD_COUNT)  # 3,000 rows at a time
                if not batch:
                    break

                file_path = os.path.join(table_definitions['path'], table_partition)
                file_name = f"{table_definitions['file_name']}_{Utils.generate_sequence(FILE_SEQUENCE_LENGTH, file_sequence)}_{table_partition}.csv"
                persist_record(batch, file_path, file_name)
                file_sequence = file_sequence + 1

                # for row in batch:
                #     logger.info(row)
                # exit()

            proxy.close()

            logger.info(f"started processing partition {schema} - {table_partition}")

        else:
            # Fetch all results
            query = text(sql)
            results = engine.execute(query).fetchall()

            logger.info(f"records - {len(results)}")

            exit()

            file_sequence = 0
            for i in range(0, len(results), FILE_RECORD_COUNT):
                logger.info(f"{i} - {i + FILE_RECORD_COUNT}")
                batch = results[i:i + FILE_RECORD_COUNT]
                if HEADERS:
                    df = pd.DataFrame(batch, columns=TABLE_HEADERS)
                else:
                    df = pd.DataFrame(batch)
                file_path = os.path.join(table_definitions['path'], table_partition)
                file_name = f"{table_definitions['file_name']}_{Utils.generate_sequence(FILE_SEQUENCE_LENGTH, file_sequence)}_{table_partition}.csv"
                logger.info(file_name)
                df.to_csv(file_name, sep=',', encoding='utf-8', index=False)

                logger.info(df.to_string())
                file_sequence = file_sequence + 1

        end_time = time.time()
        logger.info(f"completed processing partition {schema} - {table_partition} in {end_time - start_time}")


if __name__ == '__main__':

    logger.info(f"querying - {table_name}")
    logger.info(f"start_date - {start_date}")
    logger.info(f"end_date - {end_date}")

    schemas = Utils.generate_schema_names(tables_schema_mapping[table_name], start_date, end_date)
    partitions = pd.date_range(start_date, datetime.strptime(end_date, '%Y-%m-%d') - timedelta(days=1), freq='d').strftime('%Y%m%d').tolist()
    # logger.info(partitions)
    for schema_name in schemas:
        process_cdr(tables_schema_mapping[table_name], schema_name, table_name, partitions)
