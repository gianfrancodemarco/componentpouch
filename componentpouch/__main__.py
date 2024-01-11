import typer

from .tools import app as tools
from .repo import app as repo

app = typer.Typer(no_args_is_help=True)
app.add_typer(tools, name="tools")
app.add_typer(repo, name="repo")

if __name__ == "__main__":
    app()