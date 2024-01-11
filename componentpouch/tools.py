import subprocess
from typing import List

import typer

app = typer.Typer()

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

@app.command(name='list')
def _list():
    for tool in allowed_tools:
        typer.echo(tool)

@app.command()
def install(
    tools: List[str] = typer.Argument(..., help="List of tools to install (used with 'install' command)", autocompletion=lambda: list(allowed_tools.keys())),
):
    """Install required tools"""
    for tool in tools:
        if tool.lower() not in allowed_tools:
            typer.echo(f"Error: {tool} is not a valid tool. Valid tools are: {', '.join(allowed_tools)}")
            raise typer.Abort()

        typer.echo(f"Installing {tool}...")
        allowed_tools[tool.lower()]()


if __name__ == "__main__":
    app()