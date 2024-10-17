import pandas as pd
import random


def pick_random_user():
    # UserAnimeList.csv has this number of lines
    lines_count = 10000  # TODO: change to 80329337
    """
    with open('UserAnimeList.csv', 'r') as f:
        count = sum(1 for _ in f)
        print(count)
        """

    chosen = random.randint(0, lines_count)

    df = pd.read_csv("UserAnimeList.csv",
                     skiprows=chosen, nrows=1)

    username = df.iloc[0, 0]
    return username


def get_user_data(username):
    df = pd.DataFrame()
    # assuming user data is not fragmented
    userfound = False

    for slice in pd.read_csv('UserAnimeList.csv', chunksize=100000,
                             usecols=["username", "anime_id",
                                      "my_score", "my_status"]):
        slice = pd.DataFrame(slice)

        user_slice = slice.loc[slice['username'] == username]
        if not userfound:
            if ~user_slice.empty:
                # first entries found for that user
                userfound = True
        # not 'else' on purpose
        if userfound:
            if user_slice.empty:
                # no more entries for that user
                break
            df = pd.concat([df, user_slice])

    return df.loc[df['my_status'].isin([1, 2])]
