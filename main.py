from anime import get_all_genres, get_all_anime, vectorize_anime, get_example
import pandas as pd
from user import pick_random_user, get_user_data
import numpy as np
from regression import linear_reg
from randomforest import random_forest
from svm import svm

def main():
    anime_df = get_all_anime()

    # username = pick_random_user()
    # this user was picked because he has a small number of anime
    # and they fit nicely to a print
    # TODO: return to what it was
    username = "terune_uzumaki"
    user_df = get_user_data(username)

    user_anime_df = anime_df.loc[anime_df['anime_id'].isin(
        user_df['anime_id'])]

    assert user_anime_df.shape[1] == anime_df.shape[1]

    X_train = vectorize_anime(user_anime_df)
    y_train = user_df['my_score'].to_numpy()

    # from anime_df pick random X animes (X=1000)
    X_all = vectorize_anime(anime_df)

    # HERE we have all we need to start work
    y1_pred = linear_reg(X_train[:,1:], y_train, X_all[:,1:])
    y2_pred = random_forest(X_train[:,1:], y_train, X_all[:,1:])
    y3_pred = svm(X_train[:,1:], y_train, X_all[:,1:])
    
    # run those animes into regression model and pick top 3
    top_three = np.sort(y1_pred)[:3]  # need to make sure index is appropiate
    # print those names


if __name__ == "__main__":
    main()
