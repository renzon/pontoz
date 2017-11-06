from pontoz.bigquery.client import client

QUERY = (
    'SELECT sale, pointz_sale FROM `pontoz.transactions` '
)
query_job = client.query(QUERY)  # API request
rows = query_job.result()  # Waits for query to finish

for row in rows:
    print(row.name)
