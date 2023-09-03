from datetime import date, datetime
from dateutil.relativedelta import relativedelta


class Utils:

    @staticmethod
    def generate_sequence(req_len: int, seq):
        return '0'*(req_len - len(str(seq))) + str(seq)

    @staticmethod
    def generate_schema_names(tables_schema_map, start_date: str, end_date: str) -> list[str]:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")

        start_date = start_date.replace(day=1)
        end_date = end_date.replace(day=1)
        dates = []
        dates_years = []
        current_year = start_date.year
        while start_date <= end_date:

            if start_date.year != current_year:
                current_year = start_date.year

                dates.append(dates_years)

                dates_years = []

            schema = None
            if tables_schema_map['date_str'] == 'MONTH_YEAR':
                dated = start_date.strftime("%b_%y")
                schema = f"{tables_schema_map['schema_prefix']}_{dated}"
            elif tables_schema_map['date_str'] == 'YEARMONTH':
                dated = start_date.strftime("%Y%m")
                schema = f"{tables_schema_map['schema_prefix']}_{dated}"

            dates_years.append(schema.upper())

            start_date += relativedelta(months=1)

        else:
            if len(dates_years) > 0:
                dates.append(dates_years)

        return dates_years
