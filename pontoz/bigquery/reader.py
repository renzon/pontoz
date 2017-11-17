from datetime import date

from google.cloud import bigquery

from pontoz.bigquery.client import client

ANNUAL_DRE_QUERY = """
SELECT
  SUM(sale) AS sale,
  SUM(pointz_sale) AS pointz_sale,
  year,
  month,
  region_name,
  client_name,
  segment_name
FROM
  `pontoz.transactions`
WHERE
  year = @year
GROUP BY
  segment_name,
  client_name,
  region_name,
  month,
  year
ORDER BY
  segment_name,
  client_name,
  region_name,
  month,
  year
"""


def get_annual_dre_by_client_region(year=None):
    if year is None:
        year = date.today().year
    year = int(year)
    year_param = bigquery.ScalarQueryParameter('year', 'INT64', year)
    job_config = bigquery.QueryJobConfig()
    job_config.query_parameters = [year_param]
    query_job = client.query(
        ANNUAL_DRE_QUERY, job_config=job_config)  # API request - starts the query

    # Waits for the query to finish
    return query_job.result()


MAX_TRANSACTION_ID_QUERY = """
SELECT
  MAX(id) as max_id
FROM
  `pontoz.transactions`
"""


def get_max_transaction_id():
    job_config = bigquery.QueryJobConfig()
    query_job = client.query(MAX_TRANSACTION_ID_QUERY, job_config=job_config)  # API request - starts the query

    # Waits for the query to finish
    row = list(query_job.result())[0]
    return row.max_id if row.max_id is not None else 0


if __name__ == '__main__':
    # annual_reports = get_annual_dre_by_client_region()
    # print(list(annual_reports))
    print(get_max_transaction_id())
