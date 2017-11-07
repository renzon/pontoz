from os import path

from google.cloud import bigquery

from pontoz.bigquery.client import client

dataset = client.dataset('pontoz')

_json_file_path = path.dirname(__file__)
_json_file_path = path.join('fixtures', 'transactions.json')

table_ref = dataset.table('transactions')
job_config = bigquery.LoadJobConfig()
job_config.source_format = 'NEWLINE_DELIMITED_JSON'

with open(_json_file_path, 'rb') as file:
    job = client.load_table_from_file(
        file, table_ref, job_config=job_config)  # API request
    job.result()  # Waits for table load to complete.
