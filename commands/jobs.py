from datetime import datetime

import requests
from rich.console import Console
from rich.table import Table

from util.check_access_token import get_token
from util.common_login import common_login
import config

console = Console()


def list_jobs_command():
    token = get_token()
    if len(token) > 0:
        apiurl = f'{config.api_base_url}/job/jobs-queue'
        jobs = requests.get(apiurl, headers={'Authorization': f'Bearer {token}'})
        if jobs.status_code == 200:
            jobs_json = jobs.json()
            table = Table(show_header=True, header_style='bold blue')
            table.add_column("JobId", justify="left")
            table.add_column("JobType", justify="left")
            table.add_column("UserId", justify="left")
            table.add_column("Status", justify="left")
            table.add_column("Started", justify="left")
            table.add_column("Ended", justify="left")
            sliced = jobs_json[0:10]
            for job in sliced:
                table.add_row(job["id"], job["jobType"], job["userId"], job["status"],
                              str(format_date_time(job["datetime"])),
                              str(format_date_time(job["enddatetime"])))
            console.print(table)
        else:
            console.print(
                f"[bold red]Invalid Access Token. Try logging in again and re-run the same command again [/bold "
                f"red]")
            common_login()


def format_date_time(epoch):
    try:
        return datetime.fromtimestamp(epoch / 1000)
    except:
        return '-'
