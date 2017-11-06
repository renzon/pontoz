from google.api_core.exceptions import NotFound
from google.cloud.bigquery import SchemaField
from google.cloud.bigquery.table import Table

from pontoz.bigquery.client import client

for pontoz_dataset in client.list_datasets():
    pass
transactions_ref = pontoz_dataset.table('transactions')
try:
    transactions_table = client.get_table(transactions_ref)
except NotFound:
    transactions_table = Table(transactions_ref)
    SCHEMA = [
        SchemaField('id', 'integer', 'REQUIRED', None, ()),
        SchemaField('sale', 'float', 'REQUIRED', None, ()),
        SchemaField('pointz_sale', 'float', 'REQUIRED', None, ()),
        SchemaField('year', 'integer', 'REQUIRED', None, ()),
        SchemaField('month', 'integer', 'REQUIRED', None, ()),
        SchemaField('day', 'integer', 'REQUIRED', None, ()),
        SchemaField(
            'store', 'record', 'REQUIRED', None,
            (
                SchemaField('name', 'string', 'REQUIRED', None, ()),
                SchemaField('id', 'integer', 'REQUIRED', None, ()),
                SchemaField(
                    'region', 'record', 'REQUIRED', None,
                    (
                        SchemaField('name', 'string', 'REQUIRED', None, ()),
                        SchemaField('id', 'integer', 'REQUIRED', None, ()),
                        SchemaField(
                            'client', 'record', 'REQUIRED', None, (
                                SchemaField('segment', 'string', 'REQUIRED', None, ()),
                                SchemaField('name', 'string', 'REQUIRED', None, ()),
                                SchemaField('id', 'integer', 'REQUIRED', None, ()))
                        )
                    )
                ),
            )
        )

    ]

    transactions_table.schema = SCHEMA
    transactions_table = client.create_table(transactions_table)

    print(transactions_table)
