# knn_recommender.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
from rapidfuzz import process

class KNNProductRecommender:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)

        if 'name' not in self.df.columns:
            raise ValueError("CSV must contain a 'name' column.")

        self.df['name'] = self.df['name'].fillna('').str.lower()
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df['name'])

        self.knn_model = NearestNeighbors(metric='cosine', algorithm='brute')
        self.knn_model.fit(self.tfidf_matrix)

    def _fuzzy_match_name(self, query):
        names = self.df['name'].tolist()
        match, score, _ = process.extractOne(query.lower(), names)
        return match if score >= 60 else None

    def recommend(self, product_name, top_n=5):
        matched_name = self._fuzzy_match_name(product_name)

        if not matched_name:
            return pd.DataFrame(), None

        idx = self.df[self.df['name'] == matched_name].index[0]
        product_vector = self.tfidf_matrix[idx]

        distances, indices = self.knn_model.kneighbors(product_vector, n_neighbors=top_n + 1)
        recommended_indices = indices[0][1:]  # Skip self
        return self.df.iloc[recommended_indices], matched_name
