import typer

from rich.table import Table
from rich.console import Console
from pishro_lib.package.models.package import Package
from pishro_lib.package.services.package_service import get_package, get_packages


def list_packages(
    repo: str = typer.Option(help="Name of the pishro repository"),
    name: str = typer.Option("", help="Name of the pishro package to show"),
):
    """
    List pishro packages in a pishro repository.

    Args:
        repo (str): Name of the pishro repository
        name (str): The name of the package to list
    """

    table = Table(title="Packages")
    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Descritpion", style="green")
    table.add_column("Version", style="magenta")

    try:
        if name:
            package: Package = get_package(repository_name=repo, package_name=name)
            table.add_row(
                package.name,
                package.description,
                package.version,
            )
        else:
            packages: list[Package] = get_packages(repository_name=repo)
            for Package in packages:
                table.add_row(
                    Package.name,
                    Package.description,
                    Package.version,
                )

        console = Console()
        console.print(table)
    except Exception as e:
        typer.echo(f"❌ Error: {str(e)}", err=True)
        raise typer.Exit(code=1)
