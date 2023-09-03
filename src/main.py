import logging
import sys
from datetime import timedelta, datetime
from sqlalchemy import engine, text
from sqlalchemy.orm import sessionmaker
from model.prepaid_rate import PrepaidRateModel
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

# engine = engine.create_engine("postgresql://%s:%s@%s/%s" % ('db_user', 'pass', 'host', 'db_name'))
# factory = sessionmaker(bind=engine)
# session = factory()

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


def process_cdr(cdr_type: str, partition_name):
    # session.query()
    ...


if __name__ == '__main__':
    # session.query(PrepaidRateModel).filter(PrepaidRateModel.date_key)
    table_name = 'FCT_CDR_RECHARGE'
    logger.info(table_name)
    logger.info(tables_schema_mapping[table_name])
    schemas = Utils.generate_schema_names(tables_schema_mapping[table_name], START_DATE, END_DATE)
    partitions = pd.date_range(START_DATE, datetime.strptime(END_DATE, '%Y-%m-%d') - timedelta(days=1), freq='d')
    logger.info(schemas)
    logger.info(partitions)
