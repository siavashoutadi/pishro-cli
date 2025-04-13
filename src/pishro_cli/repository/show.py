import typer
from pishro_lib.git.services.repository_service import get_repository
from rich.table import Table
from rich.console import Console


def show_repository(
    name: str = typer.Argument(..., help="Name of the repository to show"),
):
    """
    Show details of a git repository
    """
    try:
        repo = get_repository(name)
        table = Table(title="Repository")
        table.add_column("Name", style="cyan", no_wrap=True)
        table.add_column("URL", style="magenta")
        table.add_column("Branch", style="green")
        table.add_row(repo.name, repo.url, repo.branch)
        console = Console()
        console.print(table)
    except Exception as e:
        typer.echo(f"❌ Error: {str(e)}", err=True)
        raise typer.Exit(code=1)
