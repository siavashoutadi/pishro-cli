import typer

from pathlib import Path
from pishro_lib.package.services.package_service import init_package as init


def init_package(
    package_name: str = typer.Option(
        "my_package", help="Name of the package", prompt=True
    ),
    package_path: Path = typer.Option(
        "./my_package", help="Path to pishro packages directory", prompt=True
    ),
):
    init(package_path=package_path, package_name=package_name)

    typer.echo(
        f"Package '{package_name}' has been successfully initialized at '{package_path}'."
    )
