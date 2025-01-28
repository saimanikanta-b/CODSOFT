import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import linear_kernel
movies_data = {
    'title': ['Movie A', 'Movie B', 'Movie C', 'Movie D'],
    'genres': ['Action|Adventure', 'Action|Sci-Fi', 'Adventure|Fantasy', 'Sci-Fi|Fantasy'],
    'description': [
        'An action-packed adventure in space.',
        'A thrilling sci-fi story of survival.',
        'A fantasy adventure in a magical land.',
        'A sci-fi journey through time.'
    ]
}
movies = pd.DataFrame(movies_data)
ratings_data = {
    'user_id': ['User1', 'User2', 'User3', 'User1', 'User2', 'User3'],
    'movie_title': ['Movie A', 'Movie A', 'Movie A', 'Movie B', 'Movie B', 'Movie C'],
    'rating': [5, 4, 3, 4, 5, 2]
}
ratings = pd.DataFrame(ratings_data)
def content_based_recommendation(movie_title, movies_df):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(movies_df['genres'] + ' ' + movies_df['description'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    idx = movies_df.index[movies_df['title'] == movie_title].tolist()[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:3] 
    movie_indices = [i[0] for i in sim_scores]
    return movies_df['title'].iloc[movie_indices].tolist()
if name == "main":
    x=input("Enter Movie Name:")
    print(f"Content-Based Recommendations for 'Movie {x}'")
    print(content_based_recommendation(f'Movie {x}', movies))