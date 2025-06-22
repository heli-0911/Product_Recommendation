import streamlit as st
import pandas as pd
from recommender import KNNProductRecommender

# Set page config first
st.set_page_config(page_title="🛒 Product Recommender", layout="wide")

@st.cache_resource
def load_model():
    return KNNProductRecommender("All Electronics.csv")

model = load_model()
df = model.df

st.title("🛍️ Product Recommender System")
st.markdown("Select a product and apply filters to refine results:")

# ========== 🔧 SIDEBAR ==========
st.sidebar.header("Filters")

# Product dropdown
product_names = sorted(df['name'].dropna().unique().tolist())
selected_product = st.sidebar.selectbox("🔍 Choose a product:", product_names)

# Price filter (discount_price)
if 'discount_price' in df.columns and pd.api.types.is_numeric_dtype(df['discount_price']):
    min_price = int(df['discount_price'].min())
    max_price = int(df['discount_price'].max())
    price_range = st.sidebar.slider("💰 Price Range (Discounted)", min_price, max_price, (min_price, max_price))
else:
    price_range = (None, None)

# Main category filter
if 'main_category' in df.columns:
    categories = sorted(df['main_category'].dropna().unique())
    selected_categories = st.sidebar.multiselect("🏷️ Main Category", categories, default=categories)
else:
    selected_categories = None

# Ratings filter
if 'ratings' in df.columns and pd.api.types.is_numeric_dtype(df['ratings']):
    min_rating = float(df['ratings'].min())
    max_rating = float(df['ratings'].max())
    rating_threshold = st.sidebar.slider("⭐ Minimum Rating", min_rating, max_rating, min_rating)
else:
    rating_threshold = None

# Sorting
sort_by = st.sidebar.selectbox(
    "🔽 Sort by",
    ["Lowest Price", "Highest Rating", "Default"],
    index=0  # default selected option is "Lowest Price"
)



# ========== 🚀 RECOMMENDATIONS ==========
if selected_product:
    results_df, matched_name = model.recommend(selected_product, top_n=10)

    if not results_df.empty:
        st.success(f"Best match found: **{matched_name.title()}**")

        # Apply filters
        if price_range != (None, None):
            results_df = results_df[
                (results_df['discount_price'] >= price_range[0]) &
                (results_df['discount_price'] <= price_range[1])
            ]
        if selected_categories:
            results_df = results_df[results_df['main_category'].isin(selected_categories)]
        if rating_threshold is not None:
            results_df = results_df[results_df['ratings'] >= rating_threshold]

        # Apply sorting
        if sort_by == "Lowest Price":
            results_df = results_df.sort_values(by='discount_price', ascending=True)
        elif sort_by == "Highest Rating":
            results_df = results_df.sort_values(by='ratings', ascending=False)

        # Display results
        if results_df.empty:
            st.warning("No products found after applying filters.")
        else:
            for _, row in results_df.iterrows():
                st.markdown(f"### {row['name'].title()}")

                if 'image' in row and pd.notna(row['image']):
                    st.image(row['image'], width=200)

                st.markdown(f"💰 **Discounted Price:** {row.get('discount_price', 'N/A')}")
                st.markdown(f"💸 **Original Price:** {row.get('actual_price', 'N/A')}")
                st.markdown(f"⭐ **Rating:** {row.get('ratings', 'N/A')} ({row.get('no_of_ratings', 0)} ratings)")

                if 'link' in row and pd.notna(row['link']):
                    st.markdown(f"[🔗 View Product]({row['link']})")

                st.markdown("---")
    else:
        st.warning("❌ No similar products found.")
