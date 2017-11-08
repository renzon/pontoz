from google.api_core.exceptions import NotFound
from google.cloud.bigquery import SchemaField
from google.cloud.bigquery.table import Table

from pontoz.bigquery.client import client

for pontoz_dataset in client.list_datasets():
    pass
_transactions_ref = pontoz_dataset.table('transactions')
try:
    transactions_table = client.get_table(_transactions_ref)
except NotFound:
    transactions_table = Table(_transactions_ref)

    SCHEMA = [
        SchemaField('id', 'INT64', 'REQUIRED', None, ()),
        SchemaField('sale', 'FLOAT64', 'REQUIRED', None, ()),
        SchemaField('pointz_sale', 'FLOAT64', 'REQUIRED', None, ()),
        SchemaField('year', 'INT64', 'REQUIRED', None, ()),
        SchemaField('month', 'INT64', 'REQUIRED', None, ()),
        SchemaField('day', 'INT64', 'REQUIRED', None, ()),
        SchemaField('store_name', 'string', 'REQUIRED', None, ()),
        SchemaField('store_id', 'INT64', 'REQUIRED', None, ()),
        SchemaField('region_name', 'string', 'REQUIRED', None, ()),
        SchemaField('region_id', 'INT64', 'REQUIRED', None, ()),
        SchemaField('client_name', 'string', 'REQUIRED', None, ()),
        SchemaField('client_id', 'INT64', 'REQUIRED', None, ()),
        SchemaField('segment_name', 'string', 'REQUIRED', None, ()),
    ]
    transactions_table.schema = SCHEMA
    transactions_table = client.create_table(transactions_table)

    print(transactions_table)
