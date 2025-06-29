# Coffee Shop Sales Analysis Dashboard

This project is an interactive sales analytics dashboard for a coffee shop, built with Streamlit. It provides key performance indicators (KPIs), advanced analytics, and visualizations to help you explore and understand sales data.

**GitHub Repository:** [Coffee-Shop-Sales-Analysis-Dashboard-Streamlit-Pandas-Plotly](https://github.com/And3m/Coffee-Shop-Sales-Analysis-Dashboard-Streamlit-Pandas-Plotly)

**Live Streamlit App:** [Open Dashboard](https://coffee-shop-sales-analysis-dashboard-app-pandas-plotly-giwlvk7.streamlit.app/)

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
   git clone https://github.com/And3m/Coffee-Shop-Sales-Analysis-Dashboard-Streamlit-Pandas-Plotly.git
   cd Coffee-Shop-Sales-Analysis-Dashboard-Streamlit-Pandas-Plotly
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

---

## Exploratory Data Analysis (EDA) & Dashboard Details

The project includes extensive EDA and interactive dashboard features to help you understand your coffee shop sales data:

### EDA Highlights
- **Descriptive Statistics:**
  - Summary statistics for all numerical columns (mean, std, min, max, quartiles).
- **Correlation Heatmap:**
  - Visualizes relationships between numerical features to identify trends and dependencies.
- **Sales Trend Over Time:**
  - Line plot showing daily sales, helping to spot seasonality and growth.
- **Boxplot of Sales by Weekday:**
  - Reveals distribution and outliers in sales for each day of the week.
- **Pie Chart of Sales by Category:**
  - Shows the proportion of sales contributed by each product category.
- **Top 10 Products by Quantity Sold:**
  - Highlights the most popular products by volume, not just revenue.
- **Monthly Sales Growth Rate:**
  - Line plot of month-over-month sales growth percentage.
- **Distribution of Unit Prices:**
  - Histogram to visualize common price points and outliers.
- **Sales by Time of Day:**
  - Bar plot to identify which part of the day generates the most sales.

### Dashboard Visuals & Interactivity
- **KPIs:**
  - Total Revenue, Total Orders, Average Order Value, Peak Sales Location (with revenue).
- **Tabs for Analysis:**
  - Monthly Sales, Location Sales, Top Products, AOV by Category, Popular Category, Peak Hour, Peak Day, Coffee Types, Data Table.
- **Advanced Features:**
  - Outlier detection, custom SQL queries, product-level drilldown, and user feedback.
- **Download Options:**
  - Download filtered data as CSV and save any chart as PNG.

### Example Screenshots & Insights

**Dashboard Overview**  
*The dashboard provides a comprehensive summary of sales KPIs, trends, and interactive filters. Users can quickly assess overall performance and drill down into specific segments for deeper analysis.*
![Dashboard Overview](assets/Dashboard%20Overview.png)

**Monthly Sales Trend**  
*This line/bar chart reveals seasonality and growth patterns. For example, sales may peak in certain months, indicating promotional periods or seasonal demand. Identifying these trends helps optimize inventory and marketing strategies.*
![Monthly Sales](assets/Monthly%20Sales.png)

**Top Products by Revenue**  
*The top 10 products by revenue highlight the best sellers. This insight helps focus on high-performing products and can inform decisions on promotions, stock, and product development.*
![Top Products](assets/Top%20Products.png)

**Sales by Location (Pie Chart)**  
*The pie chart shows the proportion of sales from each store location. This helps identify which locations are driving the most revenue and may reveal opportunities for expansion or targeted marketing.*
![Sales by Location](assets/Sales%20by%20Location.png)

**Advanced Analytics (Correlation Heatmap)**  
*The correlation heatmap uncovers relationships between numerical features such as sales, quantity, and unit price. Strong correlations can indicate key drivers of sales or potential multicollinearity in predictive models. For example, a high correlation between quantity and sales is expected, while unexpected relationships may warrant further investigation.*
![Correlation Heatmap](assets/Advanced%20Analytics.png)

---

## Author
**Vijay Andem**  
[GitHub: And3m](https://github.com/And3m)

---
Built with ❤️ using Streamlit.
