#!/usr/bin/env python

from PIL import Image, ImageOps
import subprocess
from os import rename, makedirs, devnull
from os.path import join 
from argparse import ArgumentParser
from hashlib import sha256
from tempfile import gettempdir


app_name = "thumbnail-maker"


def get_temp_dir():
    return join(f"{gettempdir()}", app_name) 


def make_id(file_path):
    file = open(file_path, "rb")
    bytes = file.read()
    hash = sha256()
    hash.update(bytes)
    file.close()
    return hash.hexdigest()


def main():
    FNULL = open(devnull, 'w')
    try:
        makedirs(get_temp_dir())
    except FileExistsError:
        pass
        
    parser = ArgumentParser(
        prog=app_name
    )
    parser.add_argument("file", nargs=1, help="Path to MP3 file")
    args = parser.parse_args()
    file_path = args.file[0]
    backup_file_path = f"{file_path}.bak"
    id = make_id(file_path)
    thumbnail_path = join(get_temp_dir(), f"{id}.jpg")
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-i", file_path,
            thumbnail_path,
        ],
        stderr=FNULL
    )
    new_thumbnail_path = join(get_temp_dir(), f"{id}.thumbnail.jpg") 
    with Image.open(thumbnail_path) as thumbnail:
        height = thumbnail.size[1]
        ImageOps.fit(thumbnail, (height, height)).save(new_thumbnail_path)

    rename(file_path, backup_file_path)
    try:
        # ever since we output file in temp dir, there is no more overwritting warning?
        subprocess.run(
            [
                "ffmpeg",
                "-y",
                "-i", backup_file_path,
                "-i", new_thumbnail_path,
                "-map", "0:0",
                "-map", "1:0",
                "-c", "copy",
                "-id3v2_version", "3",
                "-metadata:s:v", "title=\"Album cover\"",
                "-metadata:s:v", "comment=\"Cover (front)\"",
                f"{file_path}"
            ],
            stderr=FNULL
        )
    except subprocess.CalledProcessError:
        rename(backup_file_path, file_path)
    
    FNULL.close()
    
