# 🛍️ Amazon Electronics Product Recommender System

This is a machine learning-powered product recommendation system that suggests similar Amazon electronics items based on a selected product name. It uses K-Nearest Neighbors (KNN) with TF-IDF vectorization and includes features like fuzzy search, filtering by price/category/ratings, and sorting.


## 🔍 Features

- 🔎 **Fuzzy search**: Handles typos or partial product names.
- 🎯 **KNN-based recommendations**: Suggests similar products using product names.
- 💰 **Price range filter**: Filter products by discounted price.
- 🏷️ **Category filter**: Filter by main product category or brand.
- ⭐ **Ratings filter**: Minimum rating threshold.
- 🔽 **Sorting**: Sort by lowest price or highest rating.
- 🖼️ **Product info display**: Shows image, price, rating, and purchase link.

---

## 🧠 How It Works

- **Text Vectorization**: Product names are vectorized using TF-IDF.
- **Fuzzy Matching**: `RapidFuzz` is used to match partial or similar product names.
- **Similarity Search**: `sklearn.NearestNeighbors` is used to find similar items.

---


