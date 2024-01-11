# `componentpouch`

**Usage**:

```console
$ componentpouch [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `repo`
* `tools`

## `componentpouch repo`

**Usage**:

```console
$ componentpouch repo [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `clone`: Clone a repository by name
* `list`: Lst repositories with optional regex filter

### `componentpouch repo clone`

Clone a repository by name

**Usage**:

```console
$ componentpouch repo clone [OPTIONS]
```

**Options**:

* `--username TEXT`: GitHub username  [required]
* `--repo-name TEXT`: Name of the repository to clone (used with 'clone' command)  [required]
* `--help`: Show this message and exit.

### `componentpouch repo list`

Lst repositories with optional regex filter

**Usage**:

```console
$ componentpouch repo list [OPTIONS]
```

**Options**:

* `--username TEXT`: GitHub username  [required]
* `--regex TEXT`: Regex to filter repositories (used with 'list' command)
* `--help`: Show this message and exit.

## `componentpouch tools`

**Usage**:

```console
$ componentpouch tools [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `install`: Install required tools
* `list`

### `componentpouch tools install`

Install required tools

**Usage**:

```console
$ componentpouch tools install [OPTIONS] TOOLS...
```

**Arguments**:

* `TOOLS...`: List of tools to install (used with 'install' command)  [required]

**Options**:

* `--help`: Show this message and exit.

### `componentpouch tools list`

**Usage**:

```console
$ componentpouch tools list [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.
