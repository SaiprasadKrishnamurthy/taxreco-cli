from rich.console import Console
from rich.table import Table

console = Console()


def hello_command(name: str, location: str):
    console.print(f"[bold magenta]Hello {name} from {location}[/bold magenta]")
    table = Table(show_header=True, header_style='bold blue')
    table.add_column("Name", justify="left")
    table.add_row("Sai")
    table.add_row("Kris")
    console.print(table)
