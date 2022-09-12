from datetime import datetime

import requests
from rich.console import Console
import config
from util.check_access_token import get_token
from util.common_login import common_login

console = Console()


def delete_customer_linker_command(jobId):
    token = get_token()
    apiurl = f'{config.api_base_url}/job/customer-linker/{jobId}'
    jobs = requests.delete(apiurl, headers={'Authorization': f'Bearer {token}'})
    if jobs.status_code == 200:
        console.print(
            f"[bold green]Job Deleted if it exists.  [/bold "
            f"green]")
    else:
        console.print(f"[bold red]Invalid Access Token. Try logging in again and re-run the same command again [/bold "
                      f"red]")
        common_login()
