import re
import subprocess
from typing import Optional

import requests
import typer

app = typer.Typer()

@app.command()
def list(
    username: str = typer.Option(..., help="GitHub username"),
    regex: Optional[str] = typer.Option(None, help="Regex to filter repositories (used with 'list' command)"),
):
    """Lst repositories with optional regex filter"""
    try:
        # Fetch the list of repositories for the user
        response = requests.get(f"https://api.github.com/users/{username}/repos")
        response.raise_for_status()
        repos = response.json()

        if regex:
            regex_pattern = re.compile(regex)
            filtered_repos = [repo["html_url"] for repo in repos if regex_pattern.search(repo["name"])]
            typer.echo(f"Filtered Repositories with regex '{regex}':")
            for repo in filtered_repos:
                typer.echo(repo)
        else:
            typer.echo("All Repositories:")
            for repo in repos:
                typer.echo(repo["html_url"])

    except requests.RequestException as e:
        typer.echo(f"Error: Unable to list repositories. {e}")


@app.command()
def clone(
    username: str = typer.Option(..., help="GitHub username"),
    repo_name: str = typer.Option(..., help="Name of the repository to clone (used with 'clone' command)"),
):
    """Clone a repository by name"""
    try:
        repo_url = f"https://github.com/{username}/{repo_name}.git"
        subprocess.run(["git", "clone", repo_url], check=True)
        typer.echo(f"Repository '{repo_name}' cloned successfully.")
    except subprocess.CalledProcessError:
        typer.echo(f"Error: Unable to clone repository '{repo_name}'.")


if __name__ == "__main__":
    app()