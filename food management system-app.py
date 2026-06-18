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
# Univariate Analysis
# -------------------------------
st.header("📊 Univariate Analysis")

# 1. Provider Type Distribution (Pie Chart)
fig, ax = plt.subplots()
provider_counts = food["Provider_Type"].value_counts()
ax.pie(provider_counts, labels=provider_counts.index, autopct='%1.1f%%', startangle=90)
ax.set_title("Provider Type Distribution")
st.pyplot(fig)

# 2. Receiver Type Distribution (Pie Chart)
fig, ax = plt.subplots()
receiver_counts = receivers["Type"].value_counts()
ax.pie(receiver_counts, labels=receiver_counts.index, autopct='%1.1f%%', startangle=90)
ax.set_title("Receiver Type Distribution")
st.pyplot(fig)

# 3. Food Type Distribution (Bar Chart)
fig, ax = plt.subplots()
sns.countplot(x="Food_Type", data=food, ax=ax, palette="Set2")
ax.set_title("Food Type Distribution")
st.pyplot(fig)

# 4. Meal Type Distribution (Donut Chart)
fig, ax = plt.subplots()
meal_counts = food["Meal_Type"].value_counts()
ax.pie(meal_counts, labels=meal_counts.index, autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.4))
ax.set_title("Meal Type Distribution (Donut)")
st.pyplot(fig)

# -------------------------------
# Bivariate Analysis
# -------------------------------
st.header("🔗 Bivariate Analysis")

# 5. City vs Food Listings (Horizontal Bar)
city_food = food.groupby("Location").size().reset_index(name="Listings")
fig, ax = plt.subplots(figsize=(10,6))
sns.barplot(y="Location", x="Listings", data=city_food, ax=ax, palette="Blues_r")
ax.set_title("City vs Food Listings")
st.pyplot(fig)

# 6. Provider Type vs Quantity (Box Plot)
fig, ax = plt.subplots(figsize=(8,6))
sns.boxplot(x="Provider_Type", y="Quantity", data=food, ax=ax, palette="Set3")
ax.set_title("Provider Type vs Quantity (Box Plot)")
st.pyplot(fig)

# 7. Food Type vs Quantity (Violin Plot)
fig, ax = plt.subplots(figsize=(8,6))
sns.violinplot(x="Food_Type", y="Quantity", data=food, ax=ax, palette="muted")
ax.set_title("Food Type vs Quantity (Violin Plot)")
st.pyplot(fig)

# 8. Meal Type vs Quantity (Grouped Bar)
meal_qty = food.groupby("Meal_Type")["Quantity"].sum().reset_index()
fig, ax = plt.subplots(figsize=(8,6))
sns.barplot(x="Meal_Type", y="Quantity", data=meal_qty, ax=ax, palette="coolwarm")
ax.set_title("Meal Type vs Quantity")
st.pyplot(fig)

# -------------------------------
# Multivariate Analysis
# -------------------------------
st.header("🌐 Multivariate Analysis")

# 9. City + Provider Type + Quantity (Stacked Bar)
city_provider_qty = food.groupby(["Location","Provider_Type"])["Quantity"].sum().unstack().fillna(0)
fig, ax = plt.subplots(figsize=(12,6))
city_provider_qty.plot(kind="bar", stacked=True, ax=ax, colormap="tab20")
ax.set_title("City + Provider Type + Quantity (Stacked Bar)")
st.pyplot(fig)

# 10. Food Type + Meal Type + Quantity (Heatmap)
food_meal_qty = food.groupby(["Food_Type","Meal_Type"])["Quantity"].sum().unstack().fillna(0)
fig, ax = plt.subplots(figsize=(10,6))
sns.heatmap(food_meal_qty, annot=True, fmt="d", cmap="YlGnBu", ax=ax)
ax.set_title("Food Type vs Meal Type (Heatmap)")
st.pyplot(fig)

# 11. Provider + Claims + Quantity (Treemap alternative: Bar)
provider_claims = claims.merge(food, on="Food_ID").merge(providers, on="Provider_ID")
provider_claims_summary = provider_claims.groupby("Name")["Quantity"].sum().reset_index().sort_values("Quantity", ascending=False).head(10)
fig, ax = plt.subplots(figsize=(10,6))
sns.barplot(y="Name", x="Quantity", data=provider_claims_summary, ax=ax, palette="crest")
ax.set_title("Top Providers by Claims + Quantity")
st.pyplot(fig)

# 12. Receiver + Claims + Quantity (Bubble Chart)
receiver_claims = claims.merge(food, on="Food_ID").merge(receivers, on="Receiver_ID")
receiver_summary = receiver_claims.groupby("Name").agg({"Claim_ID":"count","Quantity":"sum"}).reset_index()
fig, ax = plt.subplots(figsize=(10,6))
sns.scatterplot(x="Claim_ID", y="Quantity", size="Quantity", hue="Name", data=receiver_summary, ax=ax, sizes=(50,500), legend=False)
ax.set_title("Receiver Claims vs Quantity (Bubble Chart)")
st.pyplot(fig)

# -------------------------------
# Claim Analysis
# -------------------------------
st.header("📑 Claim Analysis")

# 13. Claim Status Distribution (Pie Chart)
fig, ax = plt.subplots()
status_counts = claims["Status"].value_counts()
ax.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=90)
ax.set_title("Claim Status Distribution")
st.pyplot(fig)

# 14. Top Receivers (Horizontal Bar)
top_receivers = receiver_claims.groupby("Name")["Claim_ID"].count().reset_index().sort_values("Claim_ID", ascending=False).head(10)
fig, ax = plt.subplots(figsize=(10,6))
sns.barplot(y="Name", x="Claim_ID", data=top_receivers, ax=ax, palette="flare")
ax.set_title("Top Receivers by Claims")
st.pyplot(fig)

# 15. Top Providers (Horizontal Bar)
top_providers = provider_claims.groupby("Name")["Claim_ID"].count().reset_index().sort_values("Claim_ID", ascending=False).head(10)
fig, ax = plt.subplots(figsize=(10,6))
sns.barplot(y="Name", x="Claim_ID", data=top_providers, ax=ax, palette="rocket")
ax.set_title("Top Providers by Claims")
st.pyplot(fig)
