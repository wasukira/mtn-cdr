import logging
import sys
from typing import List
from datetime import timedelta, datetime
from sqlalchemy import engine, text
from sqlalchemy.orm import sessionmaker
from model.prepaid_rate import PrepaidRateModel
from src.model.cs5_ccn_voice_ma import Cs5CcNVoiceMA
import pandas as pd
from src.utils.utils import Utils

logging.basicConfig(format='[%(asctime)s] - [%(levelname)-8s] - [%(module)s:%(lineno)d ] - %(message)s',
                    datefmt='%Y-%m-%d:%H:%M:%S',

                    level=logging.INFO,
                    stream=sys.stdout)

logger = logging.getLogger("main")

START_DATE = '2019-04-01'
END_DATE = '2019-05-01'
tables = ['CS5_CCN_SMS_MA']
FILE_RECORD_COUNT = 3000

engine = engine.create_engine("postgresql://%s:%s@%s/%s" % ('db_user', 'pass', 'host', 'db_name'))
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
        'date_str': 'MONTH_YEAR'
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


def process_cdr(schema: str, schema_table_name, table_partitions):
    for table_partition in table_partitions:
        sql = f"SELECT * FROM {schema}.{schema_table_name} PARTITION ({table_partition})"
        logger.info(sql)
        q_count = session.query(Cs5CcNVoiceMA).from_statement(text(sql)).count
        partition_query = session.query(Cs5CcNVoiceMA).from_statement(text(sql))
        # fetch data in batches
        file_sequence = 0
        for i in range(0, q_count, FILE_RECORD_COUNT):
            batch = partition_query.slice(i, i + FILE_RECORD_COUNT)
            logger.info(batch)



        partition_records = session.query(Cs5CcNVoiceMA).from_statement(text(sql)).all()


if __name__ == '__main__':
    # session.query(PrepaidRateModel).filter(PrepaidRateModel.date_key)
    table_name = 'FCT_CDR_RECHARGE'
    logger.info(table_name)
    logger.info(tables_schema_mapping[table_name])
    schemas = Utils.generate_schema_names(tables_schema_mapping[table_name], START_DATE, END_DATE)
    partitions = pd.date_range(START_DATE, datetime.strptime(END_DATE, '%Y-%m-%d') - timedelta(days=1), freq='d').strftime('%Y%m%d').tolist()
    logger.info(partitions)
    for schema_name in schemas:
        process_cdr(schema_name, table_name, partitions)
    # process_cdr()
