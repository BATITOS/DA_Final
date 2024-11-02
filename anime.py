import pandas as pd
import numpy as np

cols = ['anime_id', 'genre', 'studio', 'producer', 'members', 'popularity',
        'episodes', 'source', 'type']

anime_data = None


def get_all_anime() -> pd.DataFrame:
    global anime_data
    if anime_data is None:
        anime_data = pd.read_csv("AnimeList.csv", usecols=cols).dropna()
    return anime_data


genres = None
genresset = None


def get_all_genres() -> set:
    global genres
    global genresset

    if genres is None or genresset is None:
        genres = pd.read_csv("AnimeList.csv", usecols=['genre']).dropna()
        genresset = set()
        for i, genrestring in enumerate(genres.iloc[:, 0].unique()):
            genresset.update({genre.strip()
                              for genre in str(genrestring).split(sep=',')})

    return genresset


example_vector = None


def init_example():
    genresset = get_all_genres()
    genreslist = list(genresset)
    genreslist.sort()

    anime_data = get_all_anime()

    studioslist = list(anime_data['studio'].unique())
    studioslist.sort()

    producerlist = list(anime_data['producer'].unique())
    producerlist.sort()

    sourcelist = list(anime_data['source'].unique())
    sourcelist.sort()

    typelist = list(anime_data['type'].unique())
    typelist.sort()

    global example_vector
    example_vector = pd.DataFrame(
        index=['anime_id'] + genreslist + studioslist + producerlist +
        ['members', 'popularity', 'episodes'] + sourcelist + typelist)

    return example_vector


init_example()


def get_example():
    global example_vector
    return example_vector
