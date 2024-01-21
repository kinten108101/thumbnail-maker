# thumbnail-maker

## Installation

pipx is recommend:

```
$ pipx install ./thumbnail-maker
Installing to existing venv 'thumbnail_maker'
  installed package thumbnail_maker 0.0.1, installed using Python 3.11.6
  These apps are now globally available
    - thumbnail-maker
done! ✨ 🌟 ✨
```

You can also use pip. However, on some Linux distributions e.g. Arch Linux, Python packages are externally managed by the distro's own package manager, so you have to create a virtual environment first:

```
$ python -m venv .my-venv
$ source ./.my-venv/bin/activate
(.my-env) $ pip install ./thumbnail-maker
Processing ./thumbnail-maker
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  [...]
Successfully installed thumbnail_maker-0.0.1
```

## Running

If this program is installed in a virtual environment (as explained above), you have to activate that environment first:

```
$ source ./.my-venv/bin/activate
(.my-venv) $
```
Otherwise, run with the `thumbnail-maker` command:
```
$ thumbnail-maker ./Music/just\ friends.mp3
Thumbnail modified for file "./Music/just friends.mp3"
Original file is backed up as "./Music/just friends.mp3.bak"
```
