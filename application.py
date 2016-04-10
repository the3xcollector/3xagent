import os
from pprint import pprint

import config


def get_movie_files(directory, extensions):
    movies = []

    dirfiles = os.listdir(directory)

    for dirfile in dirfiles:
        filepath = os.path.join(directory, dirfile)
        if os.path.isdir(filepath):
            pass
            movies.extend(get_movie_files(filepath, extensions))
        elif os.path.isfile(filepath):
            movies.append(filepath)

    movies = [movie for movie in movies if movie.endswith(tuple(extensions))]
    return movies

cfg = config.read_config()

for d in cfg['dirs']:
    files = get_movie_files(d, cfg['config']['extensions'])
    pprint(files, width=200)

    # l = os.listdir(d)
    # pprint(l)
