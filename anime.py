import pandas as pd
import numpy as np

cols = ['anime_id', 'genre', 'studio', 'producer', 'members', 'popularity',
        'episodes', 'source', 'type']


def get_all_anime():
    return pd.read_csv("AnimeList.csv", usecols=cols)


def get_all_genres():
    genres = pd.read_csv("AnimeList.csv", usecols=['genre'])
    genresset = set()
    for i, genrestring in enumerate(genres.iloc[:, 0].unique()):
        if pd.isna(genrestring):
            continue
        genresset.update({genre.strip()
                          for genre in str(genrestring).split(sep=',')})

    return genresset


def vectorize_anime(anime_data: pd.DataFrame):
    genresset = get_all_genres()
    genreslist = list(genresset)
    genreslist.sort()

    anime_genres_list = [genre.strip() for genre in str(
        anime_data['genre'].item()).split(sep=',')]
    anime_genres_list.sort()

    print(anime_genres_list)
