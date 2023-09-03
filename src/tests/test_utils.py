import pytest
from datetime import date


@pytest.mark.parametrize('start_date, end_date,generated_months', [
    ('2019-01-01', '2019-06-01', ['Jan_19', 'Feb_19', 'Mar_19', 'Apr_19', 'May_19', 'Jun_19']),
    ('2022-01-01', '2022-04-30', ['Jan_22', 'Feb_22', 'Mar_22', 'Apr_22'])
])
def test_generate_month_interval(utils, start_date, end_date, generated_months):
    months = utils.generate_month_interval(start_date=start_date, end_date=end_date)
    assert months == generated_months
