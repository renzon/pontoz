from pontoz.bigquery.client import client
from pontoz.bigquery.schema import transactions_table


def sql_transaction_to_bigquery_row(transaction):
    return (
        transaction.id,
        float(transaction.sale),
        float(transaction.pointz_sale),
        transaction.creation.year,
        transaction.creation.month,
        transaction.creation.day,
        transaction.store.name,
        transaction.store.id,
        transaction.store.region.name,
        transaction.store.region.id,
        transaction.store.region.partner.name,
        transaction.store.region.partner.id,
        transaction.store.region.partner.segment
    )


def upload_transaction_batch(transaction_batch):
    rows = [sql_transaction_to_bigquery_row(transaction) for transaction in transaction_batch]
    client.create_rows(transactions_table, rows)
