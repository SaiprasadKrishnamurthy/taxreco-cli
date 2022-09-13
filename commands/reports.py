import requests
from rich.console import Console

import config
from util.check_access_token import get_token
from util.common_login import common_login

console = Console()


def income_comparison_report_command(financial_year):
    call_api(financial_year, 'income-comparison-report')


def section_customer_wise_26as_report_command(financial_year):
    call_api(financial_year, '26as-section-customer-wise-report')


def customer_wise_reconciliation_report_command(financial_year):
    call_api(financial_year, 'customer-wise-reconciliation-summary-report-tds')


def section_wise_reconciliation_report_command(financial_year):
    call_api(financial_year, 'section-wise-reconciliation-summary-report-tds')


def customer_wise_tan_reconciliation_summary_report_tds_command(financial_year):
    call_api(financial_year, 'customer-wise-tan-reconciliation-summary-report-tds')


def call_api(financial_year, report_type):
    token = get_token()
    if len(token) > 0:
        apiurl = f'/reports/upload-miscellaneous-report-async/{str(financial_year)}/{report_type}/-1' \
                 f'?sendEmail=true&fileName={report_type}_{financial_year}'
        response = requests.get(f'{config.api_base_url}{apiurl}', headers={'Authorization': f'Bearer {token}'})
        if response.status_code == 200:
            console.print(
                f"[bold green]Submitted {str(report_type).replace('-', ' ')}"
                f"reports Job. The actual report will be emailed "
                f"to your registered email address"
                f"  [/bold "
                f"green]")
        elif response.status_code == 429:
            console.print(
                f"[bold red]Error! There's already a job running on the server. Please wait "
                f"for that to finish or kill that"
                f" job to submit a new one  [/bold "
                f"red]")
        else:
            console.print(
                f"[bold red]Invalid Access Token. Try logging in again and re-run the same command again [/bold "
                f"red]")
            common_login()
