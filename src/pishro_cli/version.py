import os
import typer

app = typer.Typer()


@app.command()
def version():
    """
    Show the application version.
    """
    with open(
        os.path.join(os.path.dirname(__file__), "..", "..", "pyproject.toml")
    ) as f:
        for line in f:
            if line.startswith("version"):
                version = line.split("=")[1].strip().strip('"')
                break
        else:
            version = "unknown"

    typer.echo(version)
