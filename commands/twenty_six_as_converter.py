import requests
from rich.console import Console

import config
from util.check_access_token import get_token
from util.common_login import common_login

console = Console()


def convert_26as_command_csv(twentysix_as_file, email, password):
    token = get_token()
    if len(token) > 0:
        call_api(email, password, token, 'csv', twentysix_as_file)


def convert_26as_command_excel(twentysix_as_file, email, password):
    token = get_token()
    if len(token) > 0:
        call_api(email, password, token, 'excel', twentysix_as_file)


def call_api(email, password, token, output_format, twentysix_as_file):
    apiurl = f'{config.api_base_url}/apps/26as-converter?format={output_format}&email={email}&password={password}'
    files = {
        'files': open(f'{twentysix_as_file}', 'rb'),
    }
    jobs = requests.put(apiurl, files=files, headers={'Authorization': f'Bearer {token}'})
    if jobs.status_code == 200:
        console.print(
            f"[bold green]Submitted 26AS converter Job. The converted {output_format} will be emailed to your "
            f"registered email address"
            f" [/bold "
            f"green]")
    elif jobs.status_code == 429:
        console.print(
            f"[bold red]Error! There's already a job running on the server. Please wait for that "
            f"to finish or kill that"
            f" job to submit a new one  [/bold "
            f"red]")
    else:
        console.print(
            f"[bold red]Invalid Access Token. Try logging in again and re-run the same command again [/bold "
            f"red]")
        common_login()
