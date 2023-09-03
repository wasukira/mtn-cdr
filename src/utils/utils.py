from datetime import date, datetime
from dateutil.relativedelta import relativedelta


class Utils:

    @staticmethod
    def generate_schema_names(tables_schema_map, start_date: str, end_date: str) -> list[str]:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")

        # truncate the dates
        start_date = start_date.replace(day=1)
        end_date = end_date.replace(day=1)

        # keep track of the series
        dates = []

        # create series by year
        dates_years = []
        current_year = start_date.year
        while start_date <= end_date:

            # if the current year is not equal to the value of startdate.year
            if start_date.year != current_year:
                # update current year
                current_year = start_date.year

                # add the dates_year to dates
                dates.append(dates_years)

                # empty dates_years
                dates_years = []

            # store the date in current year

            # if tables_schema_map

            schema = None
            if tables_schema_map['date_str'] == 'MONTH_YEAR':
                dated = start_date.strftime("%b_%y")
                schema = f"{tables_schema_map['schema_prefix']}_{dated}"
            elif tables_schema_map['date_str'] == 'YEARMONTH':
                dated = start_date.strftime("%Y%m")
                schema = f"{tables_schema_map['schema_prefix']}_{dated}"

            # dates_years.append(start_date.strftime("%b_%y"))

            dates_years.append(schema.upper())

            # add a month
            start_date += relativedelta(months=1)

        else:
            # add the last part
            if len(dates_years) > 0:
                dates.append(dates_years)

        return dates_years