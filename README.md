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

```
$ thumbnail-maker ./Music/just\ friends.mp3
Thumbnail modified for file "./Music/just friends.mp3"
Original file is backed up as "./Music/just friends.mp3.bak"
```
