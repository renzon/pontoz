from datetime import datetime
from decimal import Decimal

from db.segments import GAS
from db.tables import Transaction, Store, Region, Partner
from pontoz.bigquery.uploader import sql_transaction_to_bigquery_row


def test_sql_transaction_to_big_query_row():
    partner = Partner(id=4, name='Posto Flex', segment=GAS)
    region = Region(id=3, name='Fortaleza', partner=partner)
    store = Store(id=2, name='Posto 1', region=region)
    transaction = Transaction(
        id=1,
        store=store,
        sale=Decimal('12.00'),
        pointz_sale=Decimal('24.00'),
        creation=datetime(2017, 5, 6, 7, 8)
    )

    assert (
               1,
               Decimal('12.00'),
               Decimal('24.00'),
               2017, 5, 6,
               'Posto 1', 2,
               'Fortaleza', 3,
               'Posto Flex', 4,
               GAS) == sql_transaction_to_bigquery_row(transaction)
