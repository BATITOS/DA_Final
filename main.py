import pandas as pd
from pick_user import pick_user
import numpy as np
from data_init import find_data, create_anime_df


def main():
    username = pick_user()

    return
    user_data, y_train = find_data(
        "UserAnimeList.csv", id)  # The watching or completed
    # Enumrate geners and create vectors
    anime_df = create_anime_df("AnimeList.csv")
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
