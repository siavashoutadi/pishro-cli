import typer

from pathlib import Path
from pishro_lib.installation.services.installation_service import install_from_local


def install_package(
    name: str = typer.Option(help="Name of the pishro package to install"),
    packages_path: Path = typer.Option(
        "./pishro-packages", help="Path to pishro packages directory"
    ),
    stack_name: str = typer.Option(help="Docker swarm stack name"),
    override_values_file: Path = typer.Option(
        None, help="Path to values file to override default values"
    ),
):
    install_from_local(
        stack_name=stack_name,
        packages_dir=packages_path,
        package_name=name,
        override_values_file=override_values_file,
    )
