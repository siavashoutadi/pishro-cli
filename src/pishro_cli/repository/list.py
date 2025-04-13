import typer
from pishro_lib.git.services.repository_service import list_repositories
from rich.table import Table
from rich.console import Console


def list_repository():
    """
    List all git repositories
    """
    try:
        repos = list_repositories()

        if not repos:
            typer.echo("No repositories found")
            return

        table = Table(title="Repositories")
        table.add_column("Name", style="cyan", no_wrap=True)
        table.add_column("URL", style="magenta")
        table.add_column("Branch", style="green")

        for repo in repos:
            table.add_row(repo.name, repo.url, repo.branch)

        console = Console()
        console.print(table)
    except Exception as e:
        typer.echo(f"❌ Error: {str(e)}", err=True)
        raise typer.Exit(code=1)
