import pandas as pd
import numpy as np

cols = ['anime_id', 'title', 'genre', 'studio', 'producer', 'members',
        'popularity', 'episodes', 'source', 'type']

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


# this example vector sets the shape for the vectors of the anime
example_vector = None
g_indices = None


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

    global example_vector, g_indices
    g_indices = ['anime_id', 'members', 'popularity', 'episodes'] + genreslist\
        + studioslist + producerlist + sourcelist + typelist
    example_vector = pd.DataFrame(
        index=g_indices)

    return example_vector


init_example()


def get_example():
    global example_vector
    return example_vector


# returned array has the first column as anime_id
# anime_id shouldn't be used in training data
def vectorize_anime(anime: pd.DataFrame):
    global example_vector, g_indices
    array = np.zeros((anime.shape[0], len(g_indices)))

    i = 0
    for _, row in anime.iterrows():
        # base data
        array[i, 0] = row['anime_id']
        array[i, 1] = row['members']
        array[i, 2] = row['popularity']
        array[i, 3] = row['episodes']

        # genres
        genrestring = row['genre']
        genresset = {genre.strip()
                     for genre in str(genrestring).split(sep=',')}
        for genre in genresset:
            index = g_indices.index(genre)
            array[i, index] = 1

        # studio
        studio = row['studio']
        index = g_indices.index(studio)
        array[i, index] = 1

        # producer
        producer = row['producer']
        index = g_indices.index(producer)
        array[i, index] = 1

        # source
        source = row['source']
        index = g_indices.index(source)
        array[i, index] = 1

        # atype
        atype = row['type']
        index = g_indices.index(atype)
        array[i, index] = 1

        i += 1

    return array
