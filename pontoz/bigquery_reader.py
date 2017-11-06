from os import path

from google.cloud.bigquery import Client

_json_file_path = path.dirname(__file__)
_json_file_path = path.join(_json_file_path, '..', 'pontoz-secret.json')
_json_file_path=path.abspath(_json_file_path)

client = Client.from_service_account_json(_json_file_path)

QUERY = (
    'SELECT sale, pointz_sale FROM `pontoz.transactions` '
)
query_job = client.query(QUERY)  # API request
rows = query_job.result()  # Waits for query to finish

for row in rows:
    print(row.name)
