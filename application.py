import os
from pprint import pprint

import yaml

def save_config(config): yaml.dump(config, open('3xagent.yml', 'w'), default_flow_style=False)

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

def read_config(): return yaml.load(open('3xagent.yml', 'r'))

config = read_config()

for d in config['dirs']:
    files = get_movie_files(d, config['config']['extensions'])
    pprint(files, width=200)

    # l = os.listdir(d)
    # pprint(l)
