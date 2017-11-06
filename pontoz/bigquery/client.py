from os import path

from google.cloud.bigquery import Client

_json_file_path = path.dirname(__file__)
_json_file_path = path.join(_json_file_path, '..', '..', 'pontoz-secret.json')
_json_file_path = path.abspath(_json_file_path)
client = Client.from_service_account_json(_json_file_path)