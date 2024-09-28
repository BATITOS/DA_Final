import pandas as pd
import random


def pick_user():
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
