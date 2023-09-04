### DEPRECATED

from sqlalchemy import Column, Integer, Float, Date, Boolean, String, BigInteger
from sqlalchemy.dialects import postgresql
from sqlalchemy.ext.declarative import declarative_base

# from src.model.partition_by_date_meta import PartitionByYearMeta

# Map entities
Base = declarative_base()

TABLE_HEADERS = ['CALL_TYPE', 'RECORD_TYPE', 'CHRONO_NUMBER', 'CHARGE_PARTY_NUMBER', 'IMSI_NUMBER', 'CALLED_CALLING_NUMBER', 'CALL_FORWARD_FLAG', 'CALL_FORWARD_NUMBER',
                 'DIALED_DIGIT', 'INCOMING_TRUNK', 'OUTGOING_TRUNK', 'CALL_TIME', 'CALL_TIMESTAMP', 'CALL_DURATION', 'FAX_DATA_VOICE_SMS_FLAG', 'HOT_BILLING_FLAG', 'IMEI_NUMBER',
                 'CHARGED_PARTY_START_CELL_ID', 'TELE_SERVICE_NUMBER', 'BEARER_NUMBER', 'TON_OF_CALLED_CALLING_NUMBER', 'NP_OF_CALLED_NUMBER', 'INTERMEDIATE_CALL_TYPE',
                 'CALL_SEQUENCE_NUMBER', 'MSC_ID', 'IN_FLAG', 'CAMEL_RECORD_DATE_AND_TIME', 'CAMEL_DURATION', 'IN_SERVICE_KEY', 'SCF_ADDRESS', 'LEVEL_OF_CAMEL_SERVICE',
                 'MCR_DESTINATION_NUMBER', 'MSC_ADDRESS', 'CALL_REFERENCE_NUMBER', 'CAMEL_INIT_CF_INDICATOR', 'DEFAULT_CALL_HANDLING', 'CHANGE_FLAGS', 'DATA_VOLUME', 'CDR_TYPE',
                 'RING_DURATION', 'CHARGING_PARTY_END_CELL_ID', 'OTHER_PARTY_START_CELL_ID', 'OTHER_PARTY_END_CELL_ID', 'BALANCE_BEFORE_EVENT', 'BALANCE_AFTER_THE_EVENT',
                 'EVENT_AMOUNT', 'DA_VALUE_BEFORE_CALL', 'DA_VALUE_AFTER_CALL', 'DA_ID', 'DA_AMOUNT_USED', 'DA_ACCOUNT_USED', 'FRIENDS_AND_FAMILY_IND', 'NET_FLAG', 'PEAK_FLAG',
                 'LAI', 'ZONE_TYPE', 'ZONE_ID_1', 'ZONE_ID_2', 'ZONE_ID_3', 'COMMUNITY_INDICATOR_SELECTED', 'FRIENDS_AND_FAMILY_NUMBER', 'RATED_UNITS_FREE_UNITS',
                 'RATED_UNITS_DEBIT', 'RATED_UNITS_CREDIT', 'OFFER_ID', 'OFFER_TYPE', 'BONUS_AMOUNT', 'ACCOUNT_GROUP_ID', 'PAM_SERVICE_ID', 'PAM_CLASS_ID', 'SELECTION_TREE_TYPE',
                 'SERVED_ACCOUNT', 'SERVED_OFFERINGS', 'TERMINATION_CAUSE', 'CHARGING_CONTEXT_ID', 'SERVICE_CONTEXT_ID', 'SERVICE_SESSION_ID', 'MSISDN_NSK', 'SERVICE_CLASS_ID',
                 'PAYTYPE', 'CALL_REFERENCE_ID', 'MA_AMOUNT_USED', 'SERVICE_IDENTIFIER', 'FLEX_5_TXT', 'AUTHORIZED_CHARGING_RULES', 'AUTHORIZED_QOS', 'CAUSE_CODE',
                 'CORRELATION_ID', 'CREDIT_CONTROL_RECORDS', 'CREDIT_CTL_FAILURE_HANDLING', 'FIRST_CALL_INFO', 'LAST_PARTIAL_OUTPUT', 'NODE_NAME', 'NON_SERVED_SUBSCRIPTION_ID',
                 'ORIGINAL_CALLED_PARTY_NUMBER', 'OUTGOING_SESSION_ID', 'RECORD_ID_NR', 'RESULT_CODE', 'RESULT_CODE_EXTENSION', 'SERVED_SUBSCRIPTION_ID', 'SERVING_ELEMENT',
                 'SUPPRESSION_AT_FORWARDING', 'USED_START_PULSES', 'USED_UNCHARGED_SERVICE_UNITS', 'USER_SESSION_ID']


class Cs5CcNVoiceMA(Base):
    __tablename__ = "ccn_voice"
    CALL_TYPE = Column(String, primary_key=True)
    RECORD_TYPE = Column(String)
    CHRONO_NUMBER = Column(String)
    CHARGE_PARTY_NUMBER = Column(String)
    IMSI_NUMBER = Column(String)
    CALLED_CALLING_NUMBER = Column(String, primary_key=True)
    CALL_FORWARD_FLAG = Column(String)
    CALL_FORWARD_NUMBER = Column(String)
    DIALED_DIGIT = Column(String)
    INCOMING_TRUNK = Column(String)
    OUTGOING_TRUNK = Column(String)
    CALL_TIME = Column(String, primary_key=True)
    CALL_TIMESTAMP = Column(Date, primary_key=True)
    CALL_DURATION = Column(Integer)
    FAX_DATA_VOICE_SMS_FLAG = Column(String)
    HOT_BILLING_FLAG = Column(String)
    IMEI_NUMBER = Column(String)
    CHARGED_PARTY_START_CELL_ID = Column(String)
    TELE_SERVICE_NUMBER = Column(String)
    BEARER_NUMBER = Column(String)
    TON_OF_CALLED_CALLING_NUMBER = Column(String)
    NP_OF_CALLED_NUMBER = Column(String)
    INTERMEDIATE_CALL_TYPE = Column(String)
    CALL_SEQUENCE_NUMBER = Column(String)
    MSC_ID = Column(String)
    IN_FLAG = Column(String)
    CAMEL_RECORD_DATE_AND_TIME = Column(Date)
    CAMEL_DURATION = Column(String)
    IN_SERVICE_KEY = Column(String)
    SCF_ADDRESS = Column(String)
    LEVEL_OF_CAMEL_SERVICE = Column(String)
    MCR_DESTINATION_NUMBER = Column(String)
    MSC_ADDRESS = Column(String)
    CALL_REFERENCE_NUMBER = Column(String)
    CAMEL_INIT_CF_INDICATOR = Column(String)
    DEFAULT_CALL_HANDLING = Column(String)
    CHANGE_FLAGS = Column(String)
    DATA_VOLUME = Column(String)
    CDR_TYPE = Column(String)
    RING_DURATION = Column(String)
    CHARGING_PARTY_END_CELL_ID = Column(String)
    OTHER_PARTY_START_CELL_ID = Column(String)
    OTHER_PARTY_END_CELL_ID = Column(String)
    BALANCE_BEFORE_EVENT = Column(String)
    BALANCE_AFTER_THE_EVENT = Column(String)
    EVENT_AMOUNT = Column(String)
    DA_VALUE_BEFORE_CALL = Column(String)
    DA_VALUE_AFTER_CALL = Column(String)
    DA_ID = Column(String)
    DA_AMOUNT_USED = Column(String)
    DA_ACCOUNT_USED = Column(String)
    FRIENDS_AND_FAMILY_IND = Column(String)
    NET_FLAG = Column(String)
    PEAK_FLAG = Column(String)
    LAI = Column(String)
    ZONE_TYPE = Column(String)
    ZONE_ID_1 = Column(String)
    ZONE_ID_2 = Column(String)
    ZONE_ID_3 = Column(String)
    COMMUNITY_INDICATOR_SELECTED = Column(String)
    FRIENDS_AND_FAMILY_NUMBER = Column(String)
    RATED_UNITS_FREE_UNITS = Column(String)
    RATED_UNITS_DEBIT = Column(String)
    RATED_UNITS_CREDIT = Column(String)
    OFFER_ID = Column(String)
    OFFER_TYPE = Column(String)
    BONUS_AMOUNT = Column(String)
    ACCOUNT_GROUP_ID = Column(String)
    PAM_SERVICE_ID = Column(String)
    PAM_CLASS_ID = Column(String)
    SELECTION_TREE_TYPE = Column(String)
    SERVED_ACCOUNT = Column(String)
    SERVED_OFFERINGS = Column(String)
    TERMINATION_CAUSE = Column(String)
    CHARGING_CONTEXT_ID = Column(String)
    SERVICE_CONTEXT_ID = Column(String)
    SERVICE_SESSION_ID = Column(String)
    MSISDN_NSK = Column(Integer)
    SERVICE_CLASS_ID = Column(String)
    PAYTYPE = Column(Integer)
    CALL_REFERENCE_ID = Column(String)
    MA_AMOUNT_USED = Column(String)
    SERVICE_IDENTIFIER = Column(String)
    FLEX_5_TXT = Column(String)
    AUTHORIZED_CHARGING_RULES = Column(String)
    AUTHORIZED_QOS = Column(String)
    CAUSE_CODE = Column(String)
    CORRELATION_ID = Column(String)
    CREDIT_CONTROL_RECORDS = Column(String)
    CREDIT_CTL_FAILURE_HANDLING = Column(String)
    FIRST_CALL_INFO = Column(String)
    LAST_PARTIAL_OUTPUT = Column(String)
    NODE_NAME = Column(String)
    NON_SERVED_SUBSCRIPTION_ID = Column(String)
    ORIGINAL_CALLED_PARTY_NUMBER = Column(String)
    OUTGOING_SESSION_ID = Column(String)
    RECORD_ID_NR = Column(String)
    RESULT_CODE = Column(String)
    RESULT_CODE_EXTENSION = Column(String)
    SERVED_SUBSCRIPTION_ID = Column(String)
    SERVING_ELEMENT = Column(String)
    SUPPRESSION_AT_FORWARDING = Column(String)
    USED_START_PULSES = Column(String)
    USED_UNCHARGED_SERVICE_UNITS = Column(String)
    USER_SESSION_ID = Column(String)
