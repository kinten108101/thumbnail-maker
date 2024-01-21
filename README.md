# thumbnail-maker

## Installation

pipx is recommend:

```sh
pipx install ./thumbnail-maker
```

You can also use pip. However, on some Linux distributions e.g. Arch Linux, Python packages are externally managed by the distro's own package manager, so you have to create a virtual environment first:

```sh
python -m venv .my-venv
source ./.my-venv/bin/activate
pip install ./thumbnail-maker
```

Run with `thumbnail-maker`:

```sh
$ thumbnail-maker ./just\ friends.mp3
```
