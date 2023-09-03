from datetime import date, datetime
from dateutil.relativedelta import relativedelta


class Utils:

    @staticmethod
    def generate_month_interval(start_date: str, end_date: str) -> list[str]:
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
            dates_years.append(start_date.strftime("%b.%y"))

            # add a month
            start_date += relativedelta(months=1)

        else:
            # add the last part
            if len(dates_years) > 0:
                dates.append(dates_years)

        return dates_years

    @staticmethod
    def generate_schema_names(schema_prefix, months) -> list:
        schemas = []
        for month in months:
            schemas.append(f"{schema_prefix}_{month}")
        return schemas
