import typer
from pathlib import Path
from pishro_lib.package.services.package_service import download_package


def download(
    repo: str = typer.Option(help="Name of the pishro repository"),
    name: str = typer.Option(help="Name of the pishro package to download"),
    version: str = typer.Option(
        default="", help="Version of the pishro package to download"
    ),
    destination: Path = typer.Option(
        default="./packages/", help="Destination directory"
    ),
):
    """
    Download a package with the specified name and version.

    Args:
        repo (str): Name of the repository
        name (str): The name of the package to download
        version (str): The version of the package to download
        destination (Path): The destination directory where the package will be downloaded
    """
    try:
        download_package(
            repository_name=repo,
            package_name=name,
            version=version,
            destination=destination,
        )
        typer.echo(f"Successfully downloaded package '{name}' to '{destination}'")
    except Exception as e:
        typer.echo(f"❌ Error: {str(e)}", err=True)
        raise typer.Exit(code=1)
