import pandas as pd

cols = ['anime_id', 'genre', 'studio', 'producer', 'members', 'popularity',
        'episodes', 'source', 'type']


def get_all_anime():
    return pd.read_csv("AnimeList.csv", usecols=cols)


def vectorize_anime(anime_data: pd.DataFrame):
    # WIP
    pass
    genresset = {genre.strip() for genre in genrestring.split(sep=',')}
