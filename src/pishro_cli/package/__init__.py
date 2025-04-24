import typer
from .download import download
from .list import list_packages
from .install import install_package
from .init import init_package


app = typer.Typer(no_args_is_help=True)

app.command(name="download", help="Download a pishro package")(download)
app.command(name="list", help="List pishro packages in a pishro repository")(
    list_packages
)
app.command(name="install", help="Install pishro package")(install_package)
app.command(name="init", help="Initialize a pishro package")(init_package)
