import typer
from typing import Optional
from pishro_lib.git.models.repository import GitRepository
from pishro_lib.git.services.repository_service import (
    add_repository as add_repo_service,
)


def add_repository(
    name: str = typer.Argument(..., help="Name of the repository"),
    url: str = typer.Option(help="URL of the git repository"),
    branch: str = typer.Option("main", help="Branch to use"),
    username: Optional[str] = typer.Option(None, help="Username for authentication"),
    token: Optional[str] = typer.Option(None, help="Token for authentication"),
):
    """
    Add a new git repository
    """
    try:
        # Create a GitRepository model
        repo = GitRepository(
            name=name,
            url=url,
            branch=branch,
            username=username,
            token=token if token else None,
        )

        # Use the repository service to add the repository
        add_repo_service(repo)

        typer.echo(f"Successfully added repository '{name}' with URL {url}")
    except Exception as e:
        typer.echo(f"❌ Error: {str(e)}", err=True)
        raise typer.Exit(code=1)
