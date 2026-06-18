import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -------------------------------
# Load Data
# -------------------------------
claims = pd.read_csv("claims_data.csv")
food = pd.read_csv("food_listings_data.csv")
providers = pd.read_csv("providers_data.csv")
receivers = pd.read_csv("receivers_data.csv")

st.title("🍽️ Local Food Wastage Management - EDA Dashboard")

# -------------------------------
# Helper function for plotting
# -------------------------------
def plot_bar(data, x, title, xlabel, ylabel="Count"):
    fig, ax = plt.subplots(figsize=(8,5))
    sns.countplot(x=x, data=data, ax=ax, palette="viridis")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    st.pyplot(fig)

def plot_grouped_bar(df, x, y, title, xlabel, ylabel):
    fig, ax = plt.subplots(figsize=(8,5))
    sns.barplot(x=x, y=y, data=df, ax=ax, palette="mako")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    st.pyplot(fig)

# -------------------------------
# Univariate Analysis
# -------------------------------
st.header("📊 Univariate Analysis")

plot_bar(food, "Provider_Type", "Provider Type Distribution", "Provider Type")
plot_bar(receivers, "Type", "Receiver Type Distribution", "Receiver Type")
plot_bar(food, "Food_Type", "Food Type Distribution", "Food Type")
plot_bar(food, "Meal_Type", "Meal Type Distribution", "Meal Type")

# -------------------------------
# Bivariate Analysis
# -------------------------------
st.header("🔗 Bivariate Analysis")

# 5. City vs Food Listings
city_food = food.groupby("Location").size().reset_index(name="Listings")
plot_grouped_bar(city_food, "Location", "Listings", "City vs Food Listings", "City", "Listings")

# 6. Provider Type vs Quantity
provider_qty = food.groupby("Provider_Type")["Quantity"].sum().reset_index()
plot_grouped_bar(provider_qty, "Provider_Type", "Quantity", "Provider Type vs Quantity", "Provider Type", "Quantity")

# 7. Food Type vs Quantity
food_qty = food.groupby("Food_Type")["Quantity"].sum().reset_index()
plot_grouped_bar(food_qty, "Food_Type", "Quantity", "Food Type vs Quantity", "Food Type", "Quantity")

# 8. Meal Type vs Quantity
meal_qty = food.groupby("Meal_Type")["Quantity"].sum().reset_index()
plot_grouped_bar(meal_qty, "Meal_Type", "Quantity", "Meal Type vs Quantity", "Meal Type", "Quantity")

# -------------------------------
# Multivariate Analysis
# -------------------------------
st.header("🌐 Multivariate Analysis")

# 9. City + Provider Type + Quantity
city_provider_qty = food.groupby(["Location","Provider_Type"])["Quantity"].sum().reset_index()
fig, ax = plt.subplots(figsize=(10,6))
sns.barplot(x="Location", y="Quantity", hue="Provider_Type", data=city_provider_qty, ax=ax)
ax.set_title("City + Provider Type + Quantity")
st.pyplot(fig)

# 10. Food Type + Meal Type + Quantity
food_meal_qty = food.groupby(["Food_Type","Meal_Type"])["Quantity"].sum().reset_index()
fig, ax = plt.subplots(figsize=(10,6))
sns.barplot(x="Food_Type", y="Quantity", hue="Meal_Type", data=food_meal_qty, ax=ax)
ax.set_title("Food Type + Meal Type + Quantity")
st.pyplot(fig)

# 11. Provider + Claims + Quantity
provider_claims = claims.merge(food, on="Food_ID").merge(providers, on="Provider_ID")
provider_claims_summary = provider_claims.groupby("Name")["Quantity"].sum().reset_index().sort_values("Quantity", ascending=False).head(10)
plot_grouped_bar(provider_claims_summary, "Name", "Quantity", "Top Providers by Claims + Quantity", "Provider", "Quantity")

# 12. Receiver + Claims + Quantity
receiver_claims = claims.merge(food, on="Food_ID").merge(receivers, on="Receiver_ID")
receiver_claims_summary = receiver_claims.groupby("Name")["Quantity"].sum().reset_index().sort_values("Quantity", ascending=False).head(10)
plot_grouped_bar(receiver_claims_summary, "Name", "Quantity", "Top Receivers by Claims + Quantity", "Receiver", "Quantity")

# -------------------------------
# Claim Analysis
# -------------------------------
st.header("📑 Claim Analysis")

# 13. Claim Status Distribution
plot_bar(claims, "Status", "Claim Status Distribution", "Status")

# 14. Top Receivers
top_receivers = receiver_claims.groupby("Name")["Claim_ID"].count().reset_index().sort_values("Claim_ID", ascending=False).head(10)
plot_grouped_bar(top_receivers, "Name", "Claim_ID", "Top Receivers by Claims", "Receiver", "Claims")

# 15. Top Providers
top_providers = provider_claims.groupby("Name")["Claim_ID"].count().reset_index().sort_values("Claim_ID", ascending=False).head(10)
plot_grouped_bar(top_providers, "Name", "Claim_ID", "Top Providers by Claims", "Provider", "Claims")
