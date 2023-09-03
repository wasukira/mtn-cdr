import logging
import sys
from sqlalchemy import engine, text
from sqlalchemy.orm import sessionmaker
from model.prepaid_rate import PrepaidRateModel
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


def process_cdr(cdr_type: str, partition_name):
    # session.query()
    ...


if __name__ == '__main__':
    # session.query(PrepaidRateModel).filter(PrepaidRateModel.date_key)
    months = Utils.generate_month_interval(START_DATE, END_DATE)
    schemas = Utils.generate_schema_names(months)
    logger.info(months)
