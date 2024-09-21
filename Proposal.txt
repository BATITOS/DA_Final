1. Research question: What anime will a user most likely prefer?

2. Dataset: https://www.kaggle.com/datasets/azathoth42/myanimelist?select=AnimeList.csv
	    This link contains more than one file, we will use the "AnimeList.csv" and "UserAnimeList.csv" files.
	    In "AnimeList.csv" there are 14,478 data points, 31 features, the relevant columns are: anime_id, genre, studio, producer, members, popularity, episodes, source, type.
	    In "UserAnimeList.csv": there are 80M data points, 11 features, the relevant columns are: username, anime_id, my_score, my_status. 
				    the target column is my_score.

3. Methods: 

Overview:
- enumerate genres, studios and such data.
- Pick a user
- From his rated animes take those he's watching or completed.
- For each anime create a vector of data using the above data. For example the enumerated data, like studios, along with an entire sub-vector of genres.
- Create a matrix of all the relevant data. X_train is the above anime, y_train will be the score given to the above anime according to the user.
- Create a general matrix of all anime.
- Create a linear regression model. To map all anime to a score. (Maybe take a slice to improve run-time at the cost of accuracy)
- Pick X animes from the anime list. (This is said slice)
- Run them through the regression model and find top `num` scores. (num can be 3)
- Show the animes to the user.
