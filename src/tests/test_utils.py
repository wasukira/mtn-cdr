import pytest
from datetime import date


@pytest.mark.parametrize('start_date, end_date,generated_months', [
    ('2019-01-01', '2019-06-01', ['Jan.19', 'Feb.19', 'Mar.19', 'Apr.19', 'May.19', 'Jun.19']),
    ('2022-01-01', '2022-04-30', ['Jan.22', 'Feb.22', 'Mar.22', 'Apr.22'])
])
def test_generate_month_interval(utils, start_date, end_date, generated_months):
    months = utils.generate_month_interval(start_date=start_date, end_date=end_date)
    assert months == generated_months
