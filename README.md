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

📊 Dataset Info

| Column           | Description                  |
| ---------------- | ---------------------------- |
| `name`           | Product name                 |
| `main_category`  | Brand or high-level category |
| `sub_category`   | Specific category or type    |
| `image`          | Image URL                    |
| `link`           | Amazon or product URL        |
| `ratings`        | Average star rating          |
| `no_of_ratings`  | Total number of user ratings |
| `discount_price` | Final price after discount   |
| `actual_price`   | Original price               |

🙌 Credits
- Developed by: Heli Bhavsar and Daksh Bhavsar
- Data sourced from: Amazon product listings


