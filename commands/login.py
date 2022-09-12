import requests
from rich.console import Console
import config

console = Console()

url = f'{config.api_base_url}/login'


def login_command(userId: str, password: str):
    # Login to taxreco and get the API access token.
    creds = {'userId': userId, 'password': password}
    x = requests.post(url, json=creds)
    if x.status_code == 200:
        token_file = open(".token.txt", "w")
        token_file.write(str(x.json()['token']))
        token_file.close()
        console.print(f"[bold green]Logged in succesfully![/bold green]")
    else:
        console.print(f"[bold red]Invalid credentials[/bold red]")
