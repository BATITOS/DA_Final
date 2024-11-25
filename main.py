from anime import get_all_genres, get_all_anime, vectorize_anime, get_example
import pandas as pd
from user import pick_random_user, get_user_data
import numpy as np
from models import linear_reg, random_forest, svm


def main():
    anime_df = get_all_anime()

    username = pick_random_user()
    # this user was picked because he has a small number of anime
    # and they fit nicely to a print
    # username = "terune_uzumaki"
    user_df = get_user_data(username)

    # intersection of dataframes
    user_anime_df = anime_df.loc[anime_df['anime_id'].isin(
                                 user_df['anime_id'])]
    user_scores_df = user_df.loc[user_df['anime_id'].isin(
                                 anime_df['anime_id'])]

    assert user_anime_df.shape[1] == anime_df.shape[1]

    X_train = vectorize_anime(user_anime_df)
    y_train = user_scores_df['my_score'].to_numpy()

    # from anime_df pick random X animes (X=1000)
    
    X_all = vectorize_anime(anime_df)
    # run those animes into regression model and pick top 3
    # HERE we have all we need to start work
    y1_pred = linear_reg(X_train[:, 1:], y_train, X_all[:, 1:])
    y2_pred = random_forest(X_train[:, 1:], y_train, X_all[:, 1:])
    y3_pred = svm(X_train[:, 1:], y_train, X_all[:, 1:])

    mixed_lin = np.array([y1_pred,X_all[:,0]]).T
    mixed_rf = np.array([y2_pred,X_all[:,0]]).T
    mixed_svm = np.array([y3_pred,X_all[:,0]]).T
    
    
    top_three_lin = mixed_lin[np.argsort(mixed_lin[:,0])][::-1][:3]
    top_three_rf = mixed_lin[np.argsort(mixed_rf[:,0])][::-1][:3]
    top_three_svm = mixed_lin[np.argsort(mixed_svm[:,0])][::-1][:3]
    
    anime_ids_lin = top_three_lin[:,1]
    anime_ids_rf = top_three_rf[:,1]
    anime_ids_svm = top_three_svm[:,1]
    
    matching_titles_lin = anime_df[anime_df['anime_id'].isin(anime_ids_lin)]['title'].tolist()
    matching_titles_rf = anime_df[anime_df['anime_id'].isin(anime_ids_rf)]['title'].tolist()
    matching_titles_svm = anime_df[anime_df['anime_id'].isin(anime_ids_svm)]['title'].tolist()
   
    #Printing matching titles from linear Regression model.
    print(
    "These are the top 3 animes for you according to the Linear Regression model:\n"
    f"1. {matching_titles_lin[0]}\n"
    f"2. {matching_titles_lin[1]}\n"
    f"3. {matching_titles_lin[2]}\n"
    )
    
    #Printing matching titles from Random Forest model.
    print(
    "These are the top 3 animes for you according to the Random Forest model:\n"
    f"1. {matching_titles_rf[0]}\n"
    f"2. {matching_titles_rf[1]}\n"
    f"3. {matching_titles_rf[2]}\n"
)
    #Printing matching titles from linear regression model.
    print(
    "These are the top 3 animes for you according to the SVM model:\n"
    f"1. {matching_titles_svm[0]}\n"
    f"2. {matching_titles_svm[1]}\n"
    f"3. {matching_titles_svm[2]}"
)
    

if __name__ == "__main__":
    main()
