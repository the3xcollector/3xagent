import os
import math
from pprint import pprint

import imageio

import config
import videos


def get_movie_files(directory, extensions):
    movies = []

    try:
        dirfiles = os.listdir(directory)
    except WindowsError:
        print("No access to " + directory)
        return []

    for dirfile in dirfiles:
        filepath = os.path.join(directory, dirfile)
        if os.path.isdir(filepath):
            pass
            movies.extend(get_movie_files(filepath, extensions))
        elif os.path.isfile(filepath):
            movies.append(filepath)

    movies = [mov for mov in movies if mov.endswith(tuple(extensions))]
    return movies


cfg = config.read_config()

files = []
for d in cfg['dirs']:
    files.extend(get_movie_files(d, cfg['config']['extensions']))

# movies_meta = [videos.get_meta(mov) for mov in files[-3:]]

# pprint(movies_meta, width=200)

print("STOP")
