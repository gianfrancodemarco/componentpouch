import subprocess
from typing import List, Optional

import typer

def tools(
    command: str = typer.Argument(..., help="Tool command: list, install"),
    tools: Optional[List[str]] = typer.Option(None, help="List of tools to install (used with 'install' command)"),
):
    """Manage tools"""
    allowed_commands = ['list', 'install']

    if command not in allowed_commands:
        typer.echo(f"Error: {command} is not a valid command. Valid commands are: {', '.join(allowed_commands)}")
        raise typer.Abort()

    if command == 'list':
        typer.echo("Available tools:")
        for tool in allowed_tools:
            typer.echo(tool)
    elif command == 'install':
        if not tools:
            typer.echo("Error: List of tools is required.")
            raise typer.Abort()

        install(tools)

def install(tools: List[str]):
    """Install required tools"""

    for tool in tools:
        if tool.lower() not in allowed_tools:
            typer.echo(f"Error: {tool} is not a valid tool. Valid tools are: {', '.join(allowed_tools)}")
            raise typer.Abort()

        typer.echo(f"Installing {tool}...")
        allowed_tools[tool.lower()]()


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

def install_docker():
    typer.echo("🚀 Installing Docker...")
    subprocess.run(["sudo", "apt-get", "install", "docker-ce"])
    typer.echo("✅ Docker installation completed.")

def install_kubectl():
    typer.echo("🚀 Installing kubectl...")
    subprocess.run(["sudo", "apt-get", "install", "kubectl"])
    typer.echo("✅ kubectl installation completed.")

allowed_tools = {
    'vscode': install_vscode,
    'tmux': install_tmux,
    'k9s': install_k9s,
    'docker': install_docker,
    'kubectl': install_kubectl
}