import numpy as np


def main(id):
    user_data, y_train = find_data(users_file, id)  # The watching or completed
    anime_df = create_anime_df(file_name)  # Enumrate geners and create vectors
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
