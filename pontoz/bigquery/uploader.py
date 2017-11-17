def sql_transaction_to_bigquery_row(transaction):
    return (
        transaction.id,
        transaction.sale,
        transaction.pointz_sale,
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
