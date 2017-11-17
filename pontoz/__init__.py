import os
import shutil
from decimal import Decimal
from os import path

from pontoz.bigquery.reader import get_annual_dre_by_client_region
from pontoz.reports.business import DRESummary
from pontoz.reports.models import group_annual_region_report
from pontoz.reports.view import render


def generate_reports():
    query_result_iterator = get_annual_dre_by_client_region()
    if path.exists('build'):
        shutil.rmtree('build')
    os.mkdir('build')
    base_path = path.abspath('build')
    for client_data, monthly_reports in group_annual_region_report(query_result_iterator):
        monthly_reports = list(monthly_reports)
        for r in monthly_reports:
            r.base_coin_cost = 1
        summary = DRESummary(monthly_reports)
        dre_report = render(
            'dre.html',
            monthly_reports=monthly_reports,
            summary=summary,

            base_coin_value=Decimal('0.018'),
            **client_data
        )
        year = summary.monthly_reports[0].year
        file_name = f'{year}-{client_data["segment"]}-{client_data["client"]}-{client_data["region"]}.html'
        file_path = path.join(base_path, file_name)
        with open(file_path, 'w', encoding='utf8') as file:
            file.write(dre_report)


if __name__ == '__main__':
    generate_reports()
