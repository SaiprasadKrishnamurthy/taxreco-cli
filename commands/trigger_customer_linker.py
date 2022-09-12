import requests
from rich.console import Console

import config
from util.check_access_token import get_token
from util.common_login import common_login

console = Console()


def trigger_customer_linker_command(sales_file, twentysix_as_file):
    token = get_token()
    apiurl = f'{config.api_base_url}/job/customer-linker'
    files = {
        'salesFile': open(f'{sales_file}', 'rb'),
        '26asFile': open(f'{twentysix_as_file}', 'rb')
    }
    jobs = requests.post(apiurl, files=files, headers={'Authorization': f'Bearer {token}'})
    if jobs.status_code == 200:
        console.print(
            f"[bold green]Submitted Customer Linker Job.  [/bold "
            f"green]")
    elif jobs.status_code == 429:
        console.print(
            f"[bold red]Error! There's already a job running on the server. Please wait for that to finish or kill that"
            f" job to submit a new one  [/bold "
            f"red]")
    else:
        console.print(f"[bold red]Invalid Access Token. Try logging in again and re-run the same command again [/bold "
                      f"red]")
        common_login()
