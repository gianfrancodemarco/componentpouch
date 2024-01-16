#!/bin/bash

echo "🚀 Welcome to ComponentPouch Setup! 🚀"

# Install Poetry (if not already installed)
if command -v poetry &> /dev/null; then
    echo "🛠️  Poetry is already installed. Let's get started!"
else
    echo "🌟 Installing Poetry..."
    curl -sSL https://install.python-poetry.org | python3 -
fi

# Install the componentpouch package globally
echo "📦 Installing ComponentPouch globally..."

# Build and install the package
poetry config virtualenvs.create true
poetry build
poetry install

# Installing completion for typer
componentpouch --install-completion

echo "✨ ComponentPouch installation completed! ✨"
echo "🚀 You can now run 'componentpouch' from the command line to execute the ComponentPouch module."