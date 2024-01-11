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
    subprocess.run(["sudo", "apt-get", "update"])
    subprocess.run(["sudo", "apt-get", "install", "-y", "apt-transport-https"])
    subprocess.run(["curl",
                    "-s",
                    "https://packages.cloud.google.com/apt/doc/apt-key.gpg",
                    "|",
                    "sudo",
                    "apt-key",
                    "--keyring",
                    "/usr/share/keyrings/kubernetes-archive-keyring.gpg",
                    "add",
                    "-"])
    subprocess.run(
        [
            "echo",
            "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main",
            "|",
            "sudo",
            "tee",
            "/etc/apt/sources.list.d/kubernetes.list",
            ">",
            "/dev/null"])
    subprocess.run(["sudo", "apt-get", "update"])
    subprocess.run(["sudo", "apt-get", "install", "-y", "kubectl"])
    typer.echo("✅ kubectl installation completed.")


def install_kind():
    typer.echo("🚀 Installing kind...")
    subprocess.run(["curl", "-Lo", "/usr/local/bin/kind",
                   "https://kind.sigs.k8s.io/dl/v0.20.0/kind-linux-amd64"])
    subprocess.run(["chmod", "+x", "/usr/local/bin/kind"])
    typer.echo("✅ kind installation completed.")


def install_all():
    typer.echo("🚀 Installing all tools, might take a while...")
    install_docker()
    install_kubectl()
    install_kind()
    install_k9s()
    install_tmux()
    install_vscode()
    typer.echo("✅ All tools installation completed.")


allowed_tools = {
    '*': install_all,
    'docker': install_docker,
    'kind': install_kind,
    'kubectl': install_kubectl,
    'k9s': install_k9s,
    'tmux': install_tmux,
    'vscode': install_vscode,
}


@app.command(name='list')
def _list():
    for tool in allowed_tools:
        typer.echo(tool)


@app.command()
def install(
    tools: List[str] = typer.Argument(...,
                                      help="List of tools to install (used with 'install' command)",
                                      autocompletion=lambda: list(allowed_tools.keys())),
):
    """Install required tools"""
    for tool in tools:
        if tool.lower() not in allowed_tools:
            typer.echo(
                f"Error: {tool} is not a valid tool. Valid tools are: {', '.join(allowed_tools)}")
            raise typer.Abort()

        typer.echo(f"Installing {tool}...")
        allowed_tools[tool.lower()]()


if __name__ == "__main__":
    app()
