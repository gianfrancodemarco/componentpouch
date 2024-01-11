#!/usr/bin/env poetry run python

import re
import subprocess
from typing import Optional

import requests
import typer


def repo(
    command: str = typer.Argument(..., help="Repository command: list, clone"),
    regex: Optional[str] = typer.Option(None, help="Regex to filter repositories (used with 'list' command)"),
    repo_name: Optional[str] = typer.Option(None, help="Name of the repository to clone (used with 'clone' command)"),
    username: str = typer.Option("gianfrancodemarco", help="GitHub username"),
):
    """Manage repositories"""
    allowed_commands = ['list', 'clone']

    if command not in allowed_commands:
        typer.echo(f"Error: {command} is not a valid command. Valid commands are: {', '.join(allowed_commands)}")
        raise typer.Abort()

    if command == 'list':
        list_repos(username, regex)
    elif command == 'clone':
        clone_repo(username, repo_name)


def list_repos(username: str, regex: Optional[str] = None):
    """List repositories with optional regex filter"""
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


def clone_repo(username: str, repo_name: str):
    """Clone a repository by name"""

    if not repo_name:
        typer.echo("Error: Repository name is required.")
        raise typer.Abort()

    try:
        repo_url = f"https://github.com/{username}/{repo_name}.git"
        subprocess.run(["git", "clone", repo_url])
        typer.echo(f"Repository '{repo_name}' cloned successfully.")
    except subprocess.CalledProcessError:
        typer.echo(f"Error: Unable to clone repository '{repo_name}'.")
