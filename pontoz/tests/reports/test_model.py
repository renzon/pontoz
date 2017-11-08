from decimal import Decimal

import pytest
from google.cloud.bigquery._helpers import Row

from pontoz.reports import models
from pontoz.reports.models import MonthlyReport

ANNUAL_RESULT_PER_CLIENT = [
    Row((1.0, 13.0, 2017, 1, 'Fortaleza', 'Posto Flex', 'GAS'),
        {'sale': 0, 'pointz_sale': 1, 'year': 2, 'month': 3, 'region_name': 4, 'client_name': 5, 'segment_name': 6}),
    Row((2.0, 14.0, 2017, 2, 'Fortaleza', 'Posto Flex', 'GAS'),
        {'sale': 0, 'pointz_sale': 1, 'year': 2, 'month': 3, 'region_name': 4, 'client_name': 5, 'segment_name': 6}),
    Row((3.0, 15.0, 2017, 3, 'Fortaleza', 'Posto Flex', 'GAS'),
        {'sale': 0, 'pointz_sale': 1, 'year': 2, 'month': 3, 'region_name': 4, 'client_name': 5, 'segment_name': 6}),
    Row((4.0, 16.0, 2017, 4, 'Fortaleza', 'Posto Flex', 'GAS'),
        {'sale': 0, 'pointz_sale': 1, 'year': 2, 'month': 3, 'region_name': 4, 'client_name': 5, 'segment_name': 6}),
    Row((5.0, 17.0, 2017, 5, 'Fortaleza', 'Posto Flex', 'GAS'),
        {'sale': 0, 'pointz_sale': 1, 'year': 2, 'month': 3, 'region_name': 4, 'client_name': 5, 'segment_name': 6}),
    Row((6.0, 18.0, 2017, 6, 'Fortaleza', 'Posto Flex', 'GAS'),
        {'sale': 0, 'pointz_sale': 1, 'year': 2, 'month': 3, 'region_name': 4, 'client_name': 5, 'segment_name': 6}),
    Row((7.0, 19.0, 2017, 7, 'Fortaleza', 'Posto Flex', 'GAS'),
        {'sale': 0, 'pointz_sale': 1, 'year': 2, 'month': 3, 'region_name': 4, 'client_name': 5, 'segment_name': 6}),
    Row((8.0, 20.0, 2017, 8, 'Fortaleza', 'Posto Flex', 'GAS'),
        {'sale': 0, 'pointz_sale': 1, 'year': 2, 'month': 3, 'region_name': 4, 'client_name': 5, 'segment_name': 6}),
    Row((9.0, 21.0, 2017, 9, 'Fortaleza', 'Posto Flex', 'GAS'),
        {'sale': 0, 'pointz_sale': 1, 'year': 2, 'month': 3, 'region_name': 4, 'client_name': 5, 'segment_name': 6}),
    Row((10.0, 22.0, 2017, 10, 'Fortaleza', 'Posto Flex', 'GAS'),
        {'sale': 0, 'pointz_sale': 1, 'year': 2, 'month': 3, 'region_name': 4, 'client_name': 5, 'segment_name': 6}),
    Row((11.0, 23.0, 2017, 11, 'Fortaleza', 'Posto Flex', 'GAS'),
        {'sale': 0, 'pointz_sale': 1, 'year': 2, 'month': 3, 'region_name': 4, 'client_name': 5, 'segment_name': 6}),
    Row((12.0, 24.0, 2017, 12, 'Fortaleza', 'Posto Flex', 'GAS'),
        {'sale': 0, 'pointz_sale': 1, 'year': 2, 'month': 3, 'region_name': 4, 'client_name': 5, 'segment_name': 6}),
    Row((12.0, 24.0, 2017, 3, 'São Paulo', 'Posto Flex', 'GAS'),
        {'sale': 0, 'pointz_sale': 1, 'year': 2, 'month': 3, 'region_name': 4, 'client_name': 5, 'segment_name': 6}),
    Row((12.0, 24.0, 2017, 3, 'Fortaleza', 'Posto In Flex', 'GAS'),
        {'sale': 0, 'pointz_sale': 1, 'year': 2, 'month': 3, 'region_name': 4, 'client_name': 5, 'segment_name': 6}),
    Row((12.0, 24.0, 2017, 3, 'Fortaleza', 'Mercado Fartura', 'SUPER'),
        {'sale': 0, 'pointz_sale': 1, 'year': 2, 'month': 3, 'region_name': 4, 'client_name': 5, 'segment_name': 6})]


@pytest.mark.parametrize('row', ANNUAL_RESULT_PER_CLIENT)
def test_row_to_monthly_report(row):
    """Test that a bigquery row can be transformed into Monthly Report"""
    report = MonthlyReport.create_from_dct(row)
    assert report.pointz_sale == Decimal(row.pointz_sale)
    assert report.sale == Decimal(row.sale)
    assert report.year == row.year
    assert report.month == row.month


def test_annual_groupy_len():
    assert 4 == len(models.group_annual_region_report(ANNUAL_RESULT_PER_CLIENT))


def test_annual_groupy_client_data():
    client_data, _ = models.group_annual_region_report(ANNUAL_RESULT_PER_CLIENT)[0]
    assert client_data == {'region': 'Fortaleza',
                           'client': 'Posto Flex',
                           'segment': 'GAS'
                           }
