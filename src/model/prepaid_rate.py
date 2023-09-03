from sqlalchemy import Column, Integer, Float, Date, Boolean, String, BigInteger
from sqlalchemy.dialects import postgresql
from sqlalchemy.ext.declarative import declarative_base

# Map entities
Base = declarative_base()


class PrepaidRateModel(Base):
    __tablename__ = "table_name"
    id = Column(Integer, primary_key=True)
    external_id = Column(String)
    loan_status_id = Column(Integer)
    disbursedon_date = Column(Date)
    direction_cd = Column(String)
    source_system_cd = Column(String)
    bytes_sent_qty = Column(Integer)
    call_cost_amt = Column(Float)
    call_duration_qty = Column(Integer)
    other_nr = Column(String)
    cdr_ts = Column(Date)
    discount_amt = Column(Float)
    discount_pct = Column(Float)
    out_trunk_route_cd = Column(String)
    served_imei_nr = Column(String)
    seq_number_cd = Column(String)
    batch_id = Column(Integer)
    create_dt = Column(Date)
    apn_cd = Column(String)
    account_value_before_amt = Column(Float)
    account_value_after_amt = Column(Float)
    accumulator_amt = Column(Float)
    accumulator_used_qty = Column(Integer)
    charged_duration_qty = Column(Integer)
    dedicated_account_amt = Column(Float)
    dedicated_account_used_qty = Column(Integer)
    durations_units_qty = Column(Integer)
    faf_ind = Column(Integer)
    reverse_bill_cnt = Column(Integer)
    zero_rated_cnt = Column(Integer)
    account_group_cd = Column(String)
    balance_before_amt = Column(BigInteger)
    balance_after_amt = Column(BigInteger)
    bytes_received_qty = Column(BigInteger)
    location_cd = Column(String)
    network_cd = Column(String)
    service_offering_nr = Column(BigInteger)
    timezone_cd = Column(String)
    teleservice_cd = Column(String)
    traffic_case_nr = Column(BigInteger)
    served_msisdn_nr = Column(String)
    served_imsi_nr = Column(String)
    excise_tax_amt = Column(BigInteger)
    unitized_duration_qty = Column(Integer)
    tax_amt = Column(BigInteger)
    usage_subtype_key = Column(BigInteger)
    base_station_key = Column(BigInteger)
    number_prefix_key = Column(BigInteger)
    future_key1 = Column(BigInteger)
    currency_key = Column(BigInteger)
    package_key = Column(BigInteger)
    calling_community_key = Column(BigInteger)
    imsi_nsk = Column(BigInteger)
    msisdn_nsk = Column(BigInteger)
    date_key = Column(BigInteger)
    time_key = Column(BigInteger)
    payment_option_key = Column(BigInteger)
    apn_key = Column(BigInteger)
    discount_key = Column(BigInteger)
    out_trunk_route_key = Column(BigInteger)
    rating_rule_key = Column(BigInteger)
    usage_type_key = Column(BigInteger)
    timeband_key = Column(BigInteger)
    handset_model_key = Column(BigInteger)
    call_term_reason_key = Column(BigInteger)
    call_term_reason_cd = Column(BigInteger)
    bearerservice_cd = Column(BigInteger)
    in_bundle_cnt = Column(BigInteger)
    promo_cnt = Column(BigInteger)
    base_station_type = Column(String)
    base_station_id = Column(String)
    usage_type_cd = Column(String)
    usage_subtype_cd = Column(String)
    package_cd = Column(String)
    tariff_plan_cd = Column(String)
    currency_cd = Column(String)
    rating_rule_cd = Column(String)
    discount_cd = Column(String)
    tac = Column(String)
    payment_option_cd = Column(String)
    calling_community_cd = Column(String)
    call_reference_nr = Column(String)
    dw_subpart = Column(BigInteger)
    tax_1_amt = Column(BigInteger)
    tax_2_amt = Column(BigInteger)
    tax_3_amt = Column(BigInteger)
    flex_1_amt = Column(BigInteger)
    flex_2_amt = Column(BigInteger)
    flex_3_amt = Column(BigInteger)
    flex_4_amt = Column(BigInteger)
    flex_5_amt = Column(BigInteger)
    flex_1_txt = Column(String)
    flex_2_txt = Column(String)
    flex_3_txt = Column(String)
    flex_4_txt = Column(String)
    flex_5_txt = Column(String)
    flex_cdr_usage_1_txt = Column(String)
    flex_cdr_usage_2_txt = Column(String)
    flex_cdr_usage_3_txt = Column(String)
    flex_cdr_usage_4_txt = Column(String)
    flex_cdr_usage_5_txt = Column(String)
    flex_cdr_usage_1_amt = Column(BigInteger)
    flex_cdr_usage_2_amt = Column(BigInteger)
    flex_cdr_usage_3_amt = Column(BigInteger)
    flex_cdr_usage_4_amt = Column(BigInteger)
    flex_cdr_usage_5_amt = Column(BigInteger)
    cdr_reporting_period_nr = Column(BigInteger)
    dw_file_id = Column(BigInteger)
    dw_file_row_number = Column(BigInteger)
    end_base_station_id = Column(String)
    end_base_station_key = Column(BigInteger)
    other_base_station_id = Column(String)
    other_base_station_key = Column(BigInteger)
    other_end_base_station_id = Column(String)
    other_end_base_station_key = Column(BigInteger)
    charge_amt = Column(BigInteger)
    faf_cd = Column(String)
    full_discount_cnt = Column(BigInteger)
    full_discount_duration_qty = Column(BigInteger)
    in_trunk_route_cd = Column(String)
    in_trunk_route_key = Column(BigInteger)
    other_nr_nsk = Column(BigInteger)
    promo_product_key = Column(BigInteger)
    xdr_flex1_key = Column(BigInteger)
    xdr_flex2_key = Column(BigInteger)
