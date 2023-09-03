import logging
import sys
import os
from typing import List
from datetime import timedelta, datetime
from sqlalchemy import engine, text
from sqlalchemy.orm import sessionmaker
from model.prepaid_rate import PrepaidRateModel
from src.model.cs5_ccn_voice_ma import Cs5CcNVoiceMA, TABLE_HEADERS
import pandas as pd
from src.utils.utils import Utils
from src.utils.queries import ccn_voice_sql_stmt, pg_ccn_voice_sql_stmt

logging.basicConfig(format='[%(asctime)s] - [%(levelname)-8s] - [%(module)s:%(lineno)d ] - %(message)s',
                    datefmt='%Y-%m-%d:%H:%M:%S',

                    level=logging.INFO,
                    stream=sys.stdout)

logger = logging.getLogger("main")

FILE_RECORD_COUNT: int = 3000
FILE_SEQUENCE_LENGTH: int = 5

HEADERS = False

db_host = 'localhost'
db_user = 'airflow'
db_pass = 'airflow'
db_name = 'airflow'
db_port = 5435

engine = engine.create_engine(f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}")
factory = sessionmaker(bind=engine)
session = factory()

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


def process_cdr(table_definitions, schema: str, schema_table_name, table_partitions):

    for table_partition in table_partitions:

        sql = f"{table_definitions['sql']} {schema}.{schema_table_name} PARTITION (P_{table_partition})"

        # sql = f"{table_definitions['sql']} ccn_voice"
        # logger.info(sql)

        # Fetch all results
        query = text(sql)
        results = engine.execute(query).fetchall()

        file_sequence = 0
        for i in range(0, len(results), FILE_RECORD_COUNT):
            logger.info(f"{i} - {i + FILE_RECORD_COUNT}")
            batch = results[i:i + FILE_RECORD_COUNT]
            if HEADERS:
                df = pd.DataFrame(batch, columns=TABLE_HEADERS)
            else:
                df = pd.DataFrame(batch)
            file_name = os.path.join(table_definitions['path'],
                                     f"{table_definitions['file_name']}_{Utils.generate_sequence(FILE_SEQUENCE_LENGTH, file_sequence)}_{table_partition}.csv")
            logger.info(file_name)
            df.to_csv(file_name, sep=',', encoding='utf-8', index=False)

            logger.info(df.to_string())
            file_sequence = file_sequence + 1


if __name__ == '__main__':

    START_DATE = '2019-04-01'
    END_DATE = '2019-05-01'
    table_name = 'CS5_CCN_VOICE_MA'
    # logger.info(table_name)
    # logger.info(tables_schema_mapping[table_name])
    schemas = Utils.generate_schema_names(tables_schema_mapping[table_name], START_DATE, END_DATE)
    partitions = pd.date_range(START_DATE, datetime.strptime(END_DATE, '%Y-%m-%d') - timedelta(days=1), freq='d').strftime('%Y%m%d').tolist()
    logger.info(partitions)
    for schema_name in schemas:
        process_cdr(tables_schema_mapping[table_name], schema_name, table_name, partitions)
    # process_cdr()
