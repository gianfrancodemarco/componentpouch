#!/usr/bin/env poetry run python
import typer

from .tools import *
from .repo import *

app = typer.Typer(no_args_is_help=True)

app.command()(tools)
app.command()(repo)

if __name__ == "__main__":
    app()