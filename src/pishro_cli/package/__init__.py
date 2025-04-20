import typer
from .download import download
from .list import list_packages


app = typer.Typer(no_args_is_help=True)

app.command(name="download", help="Download a pishro package")(download)
app.command(name="list", help="List pishro packages in a pishro repository")(
    list_packages
)
