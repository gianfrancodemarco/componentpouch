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
poetry config virtualenvs.create false --local
poetry build
poetry install

# Installing completion for typer
# typer --install-completion

# Create a wrapper script in ~/.local/bin/
echo "🚀 Creating 'componentpouch' wrapper script in ~/.local/bin/"
echo '#!/bin/bash' > ~/.local/bin/componentpouch
echo 'poetry run typer componentpouch.__main__ run "$@"' >> ~/.local/bin/componentpouch
chmod +x ~/.local/bin/componentpouch

echo "✨ ComponentPouch installation completed! ✨"
echo "🚀 You can now run 'componentpouch' from the command line to execute the ComponentPouch module."
