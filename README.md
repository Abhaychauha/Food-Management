🍽️ Local Food Wastage Management Dashboard (Streamlit)

## 📌 Overview
This project is an **interactive Streamlit dashboard** designed to analyze and visualize food wastage management data. It connects surplus food providers with receivers (NGOs, shelters, individuals) and helps stakeholders understand distribution patterns, claims, and wastage reduction opportunities.

---

## 🎯 Objectives
- Build a **Streamlit app** for real-time data exploration.  
- Provide clear **EDA visualizations** (univariate, bivariate, multivariate).  
- Analyze **claims data** to identify top providers and receivers.  
- Deliver actionable **business recommendations** to reduce wastage.  

---

## 📂 Data Sources
- `food_listings_data.csv` → Provider type, food type, meal type, quantity, location.  
- `claims_data.csv` → Claim ID, status, receiver, provider, quantity.  
- `providers_data.csv` → Provider details (name, type, city).  
- `receivers_data.csv` → Receiver details (name, type, city).  

---

## ⚙️ Installation & Setup
### Local Run
```bash
pip install streamlit pandas seaborn matplotlib
streamlit run app.py
```
Open browser at **http://localhost:8501**

### Streamlit Cloud
1. Push `app.py` and CSVs to GitHub.  
2. Add `requirements.txt`:
   ```
   streamlit
   pandas
   seaborn
   matplotlib
   ```
3. Deploy via [Streamlit Cloud](https://streamlit.io/cloud).  

---

## 📊 Key Visualizations
- **Provider Type Distribution** → Pie chart of supermarkets, restaurants, grocery stores, catering services.  
- **Food Type Distribution** → Bar chart of vegetarian, vegan, non-vegetarian.  
- **Meal Type Distribution** → Donut chart of breakfast, lunch, dinner, snacks.  
- **Meal Type vs Quantity** → Bar chart comparing total quantities.  
- **Top Providers by Claims & Quantity** → Horizontal bar chart ranking providers.  

---

## 💡 Insights
- Supermarkets and restaurants are the most reliable contributors.  
- Balanced food type distribution ensures inclusivity for dietary needs.  
- Breakfast and snacks dominate donations, while lunch and dinner need boosting.  
- Claim analysis highlights bottlenecks and top-performing providers.  

---

## 🏢 Business Recommendations
1. Strengthen partnerships with supermarkets and restaurants.  
2. Launch awareness campaigns in cities with fewer listings.  
3. Encourage balanced donations across meal types for nutrition.  
4. Streamline claim management to reduce delays and wastage.  
5. Support top receivers with logistics and storage capacity.  

---

## 📌 Conclusion
This Streamlit dashboard demonstrates how **data visualization** can make food wastage management more efficient. By providing interactive charts and actionable recommendations, it empowers NGOs, shelters, and policymakers to reduce wastage, improve food security, and strengthen community impact.  


