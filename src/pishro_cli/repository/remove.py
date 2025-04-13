import typer
from pishro_lib.git.services.repository_service import (
    remove_repository as remove_repo_service,
)


def remove_repository(
    name: str = typer.Argument(..., help="Name of the repository to remove"),
):
    """
    Remove a git repository
    """
    try:
        # Confirm with the user
        if not typer.confirm(f"Are you sure you want to remove repository '{name}'?"):
            typer.echo("Operation cancelled")
            return

        # Use the repository service to remove the repository
        remove_repo_service(name)

        typer.echo(f"Successfully removed repository '{name}'")
    except Exception as e:
        typer.echo(f"Error removing repository: {str(e)}", err=True)
        raise typer.Exit(code=1)
