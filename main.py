import pandas as pd
from user import pick_random_user, get_user_data
import numpy as np
from data_init import find_data, create_anime_df
from anime import get_all_anime, vectorize_anime


def main():
    username = pick_random_user()

    user_df = get_user_data(username)

    anime_data = get_all_anime("AnimeList.csv")

    return
    # assert user_data.shape[1] == anime_df.shape[1]?
    X_train = [vectorize_anime(anime) for anime in user_data]
    # from anime_df pick random X animes (X=1000)
    X_all = [vectorize_anime(anime) for anime in anime_df[:1000]]

    # create a lingear regression model with user_data and anime_df
    # y is the user score
    y_pred = _predict(X_train, y_train, X_all)  # placeholder
    # run those animes into regression model and pick top 3
    top_three = np.sort(y_pred)[:3]  # need to make sure index is appropiate
    # print those names


if __name__ == "__main__":
    main()
