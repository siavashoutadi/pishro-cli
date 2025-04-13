import typer

from .version import app as version_app
from .repository import app as repository_app


app = typer.Typer(no_args_is_help=True)

app.add_typer(version_app)
app.add_typer(repository_app, name="repo", help="Manage git repositories")

if __name__ == "__main__":
    app()
