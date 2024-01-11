#!/usr/bin/env poetry run python

import re
import subprocess
from typing import List, Optional

import requests
import typer

app = typer.Typer(no_args_is_help=True)

def install_vscode():
    typer.echo("🚀 Installing VSCode...")
    subprocess.run(["sudo", "apt-get", "install", "code"])
    typer.echo("✅ VSCode installation completed.")

def install_tmux():
    typer.echo("🚀 Installing tmux...")
    subprocess.run(["sudo", "apt-get", "install", "tmux"])
    typer.echo("✅ tmux installation completed.")

def install_k9s():
    typer.echo("🚀 Installing k9s...")
    subprocess.run(["kubectl", "krew", "install", "k9s"])
    typer.echo("✅ k9s installation completed.")


@app.command()
def install(tools: List[str] = typer.Option(..., help="List of tools to install. Possible values: VSCode, tmux, k9s")):
    """Install required tools"""
    allowed_tools = {'vscode': install_vscode, 'tmux': install_tmux, 'k9s': install_k9s}

    for tool in tools:
        if tool.lower() not in allowed_tools:
            typer.echo(f"Error: {tool} is not a valid tool. Valid tools are: {', '.join(allowed_tools)}")
            raise typer.Abort()

        typer.echo(f"Installing {tool}...")
        allowed_tools[tool.lower()]()


@app.command()
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

if __name__ == "__main__":
    app()