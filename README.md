# Coffee Shop Sales Analysis Dashboard

This project is an interactive sales analytics dashboard for a coffee shop, built with Streamlit. It provides key performance indicators (KPIs), advanced analytics, and visualizations to help you explore and understand sales data.

## Features
- **Sidebar Filters:** Filter data by date range, location, and product category.
- **KPIs:** View total sales revenue, total orders, average order value, and peak sales location.
- **Visualizations:**
  - Monthly sales trends
  - Sales by location (pie chart)
  - Top 10 products by revenue
  - Average order value by category
  - Most popular product categories
  - Peak sales hour (highlighted bar chart)
  - Peak sales day
  - Coffee type distribution
- **Advanced Analytics:**
  - Outlier detection (Z-score)
  - Custom SQL queries (using pandasql)
  - Product-level drilldown
- **User Feedback:** Submit suggestions or issues directly from the dashboard.
- **Modern UI:** Dark theme, responsive layout, and clear labels for all charts.
- **Download:** Export filtered data as CSV.

## How to Use
1. **Clone this repository and navigate to the project folder:**
   ```sh
   git clone https://github.com/And3m/coffee-shop-sales-analysis.git
   cd coffee-shop-sales-analysis
   ```
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Run the dashboard:**
   ```sh
   streamlit run Dashboard.py
   ```
4. **Interact with the dashboard:**
   - Use the sidebar to filter data and explore different analytics.
   - Download filtered data or visualizations as needed.

## Deployment
You can deploy this dashboard for free on [Streamlit Cloud](https://streamlit.io/cloud):
- Push your code and data to a public GitHub repository.
- Sign in to Streamlit Cloud and create a new app, pointing to `Dashboard.py`.
- The app will be live at a shareable URL.

## Data
- The dashboard uses `cleaned_coffee_sales_dataset.csv` as its main data source. Make sure this file is present in the project directory.

## Author
**Vijay Andem**  
[GitHub: And3m](https://github.com/And3m)

---
Built with ❤️ using Streamlit.
