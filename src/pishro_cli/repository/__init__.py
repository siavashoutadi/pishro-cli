import typer
from .add import add_repository
from .list import list_repository
from .remove import remove_repository
from .show import show_repository


app = typer.Typer(no_args_is_help=True)

app.command(name="add", help="Add a new git repository")(add_repository)
app.command(name="list", help="List all git repositories")(list_repository)
app.command(name="remove", help="Remove a git repository")(remove_repository)
app.command(name="show", help="Show details of a git repository")(show_repository)
