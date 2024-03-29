# ComponentPouch 🧰

**ComponentPouch** is a command-line tool to set up your development environment with ease. It allows you to install and manage various development tools and repositories from the command line.

## Features

- **Tool Installation:** Install popular development tools like VSCode, tmux, k9s, Docker, and kubectl with a single command.
- **Repository Management:** List and clone your GitHub repositories effortlessly.
- **Customization:** Tailor your development environment by specifying the tools you want to install.

## Getting Started 🚀

### Prerequisites

- Python 3.10 or later.

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/gianfrancodemarco/componentpouch.git
    ```

2. Navigate to the project directory:

    ```bash
    cd componentpouch
    ```

3. Install dependencies:

    ```bash
    ./install.sh
    ```

The *componentpouch* command should now be available in your terminal.

### Usage

Run the following command to get a list of available commands:

```bash
componentpouch --help
```

## Command Reference 📚
You can find the command reference [here](COMMANDS.md).  
To regenerate the command reference after modifications, run:

```bash
typer componentpouch.__main__ utils docs --name componentpouch --output COMMANDS.md
```

## Contributing 🤝

Contributions are welcome! If you have suggestions, improvements, or find any issues, feel free to open an issue or submit a pull request.

## License 📝

This project is licensed under the MIT License - see the LICENSE file for details.

### Happy Coding! 🚀