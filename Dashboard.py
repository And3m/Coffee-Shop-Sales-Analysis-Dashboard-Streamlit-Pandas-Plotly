import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
from datetime import datetime

st.set_page_config(
    page_title="Coffee Shop Sales Dashboard",
    page_icon="☕",
    layout="wide")

alt.theme.enable("dark")

st.title('☕ Coffee Shop Sales Dashboard')

# --- Move author, About, and filter usage instructions to top of sidebar ---
# Add author and GitHub link with logo at the very top
st.sidebar.markdown("""
<div style='display: flex; align-items: center; gap: 10px;'>
    <span style='font-size: 16px;'>Created by <b>Vijay Andem</b></span>
    <a href="https://github.com/And3m" target="_blank">
        <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="28" style="vertical-align: middle; border-radius: 6px;"/>
    </a>
</div>
---
""", unsafe_allow_html=True)

# Add About section right after author
with st.sidebar.expander("About this Dashboard", expanded=False):
    st.write(
        """
        This interactive dashboard provides insights into coffee shop sales, including KPIs, trends, and product analysis. Use the filters to explore the data and download custom reports.
        """
    )
    st.info("Built with Streamlit ✨")

# Add filter usage instructions after About
with st.sidebar.expander("How to use the filters (Examples)", expanded=False):
    st.markdown("""
- **Date Range:** Select a start and end date to view sales for a specific period.  
  *Example: Select Jan 1 to Mar 31 to see Q1 sales.*
- **Location:** Choose one or more locations to analyze sales by store.  
  *Example: Select 'Downtown' to see only Downtown store sales.*
- **Category:** Filter by product category (e.g., Coffee, Tea, Food).  
  *Example: Select 'Coffee' and 'Tea' to compare beverage sales.*
    """)

# --- Sidebar Filters ---
st.sidebar.header("Filter Data")

# Load data
df = pd.read_csv('cleaned_coffee_sales_dataset.csv')

# Convert date column to datetime if not already
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Sidebar filters
date_min = df['date'].min()
date_max = df['date'].max()
date_range = st.sidebar.date_input("Date Range", [date_min, date_max], min_value=date_min, max_value=date_max)

locations = st.sidebar.multiselect("Location", options=df['location'].unique(), default=list(df['location'].unique()))
categories = st.sidebar.multiselect("Category", options=df['category'].unique(), default=list(df['category'].unique()))

# Filter data
df_filtered = df[(df['date'] >= pd.to_datetime(date_range[0])) & (df['date'] <= pd.to_datetime(date_range[1]))]
df_filtered = df_filtered[df_filtered['location'].isin(locations)]
df_filtered = df_filtered[df_filtered['category'].isin(categories)]

if 'hour' not in df_filtered.columns:
    df_filtered['hour'] = pd.to_datetime(df_filtered['time'], format='%H:%M:%S').dt.hour

# --- KPIs ---
col1, col2, col3, col4 = st.columns(4)

total_revenue = df_filtered['sales'].sum()
col1.metric("Total Sales Revenue", f"${total_revenue:,.2f}")

total_orders = df_filtered['id'].nunique()
col2.metric("Total Orders", f"{total_orders:,}")

aov = total_revenue/total_orders if total_orders > 0 else 0
col3.metric("Average Order Value (AOV)", f"${aov:.2f}")

if not df_filtered.empty:
    peak_sales_location = df_filtered.groupby('location')['sales'].sum().idxmax()
    peak_sales_location_revenue = df_filtered.groupby('location')['sales'].sum().max()
    col4.metric("Peak Sales Location", f"{peak_sales_location}", f"${peak_sales_location_revenue:,.2f}")
else:
    col4.metric("Peak Sales Location", "N/A", "$0.00")

# --- Tabs for Analysis ---
tabs = st.tabs(["Monthly Sales", "Location Sales", "Top Products", "AOV by Category", "Popular Category", "Peak Hour", "Peak Day", "Coffee Types", "Data Table"])

# --- Monthly Sales ---
with tabs[0]:
    revenue = df_filtered.groupby('month')['sales'].sum().reset_index()
    month_order = ['January', 'February', 'March', 'April', 'May', 'June']
    revenue['month'] = pd.Categorical(revenue['month'], categories=month_order, ordered=True)
    revenue = revenue.sort_values('month')
    fig1 = px.bar(
        revenue,
        x='month',
        y='sales',
        title='Sales by Month',
        labels={'sales': 'Sales', 'month': 'Month'},
        color='month',
        text_auto='.2s',
    )
    fig1.update_layout(showlegend=False, xaxis_title='Month', yaxis_title='Sales', autosize=True)
    fig1.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    st.plotly_chart(fig1, use_container_width=True)
    # Insight for Monthly Sales
    if not revenue.empty:
        top_month = revenue.loc[revenue['sales'].idxmax()]
        st.info(f"**Insight:** {top_month['month']} had the highest sales (${top_month['sales']:,.2f}).")
    else:
        st.info("No data available for the selected period.")

# --- Location Sales ---
with tabs[1]:
    location_revenue = df_filtered.groupby('location')['sales'].sum().reset_index()
    fig2 = px.pie(
        location_revenue,
        names='location',
        values='sales',
        title='Sales by Location',
        labels={'sales': 'Sales', 'location': 'Location'},
        color='location',
        hole=0.4
    )
    fig2.update_traces(textinfo='percent+label', textfont_size=12)
    fig2.update_layout(legend_title_text='Location', autosize=True)
    st.plotly_chart(fig2, use_container_width=True)
    # Insight for Location Sales
    if not location_revenue.empty:
        top_loc = location_revenue.loc[location_revenue['sales'].idxmax()]
        percent = (top_loc['sales'] / location_revenue['sales'].sum()) * 100 if location_revenue['sales'].sum() > 0 else 0
        st.info(f"**Insight:** {top_loc['location']} generated the most revenue (${top_loc['sales']:,.2f}), accounting for {percent:.1f}% of total sales.")
    else:
        st.info("No data available for the selected locations.")

# --- Top Products ---
with tabs[2]:
    product_revenue = df_filtered.groupby('product')['sales'].sum().reset_index()
    top_10_products = product_revenue.sort_values('sales', ascending = False)[0:10]
    fig3 = px.bar(
        top_10_products,
        x='sales',
        y='product',
        title='Top 10 Products by Revenue',
        labels={'product': 'Product', 'sales': 'Sales'},
        color='product',
        text_auto='.2s',
    )
    fig3.update_layout(showlegend=False, xaxis_title='Sales', yaxis_title='Product', autosize=True)
    fig3.update_traces(textfont_size=12, textposition="outside", cliponaxis=False)
    st.plotly_chart(fig3, use_container_width=True)
    # Insight for Top Products
    if not top_10_products.empty:
        top_prod = top_10_products.iloc[0]
        st.info(f"**Insight:** '{top_prod['product']}' is the best-selling product (${top_prod['sales']:,.2f}).")
    else:
        st.info("No product sales data available.")

# --- AOV by Category ---
with tabs[3]:
    category_aov = df_filtered.groupby('category')['sales'].mean().reset_index()
    category_aov = category_aov.sort_values(by='sales', ascending=False)
    fig4 = px.bar(
        category_aov,
        x='sales',
        y='category',
        title='Average Order Value by Category',
        labels={'sales': 'Average Order Value', 'category': 'Category'},
        color='category',
        text_auto='.2s',
    )
    fig4.update_layout(showlegend=False, xaxis_title='Average Order Value', yaxis_title='Category', autosize=True)
    fig4.update_traces(textfont_size=12, textposition="outside", cliponaxis=False)
    st.plotly_chart(fig4, use_container_width=True)
    # Insight for AOV by Category
    if not category_aov.empty:
        top_cat = category_aov.iloc[0]
        st.info(f"**Insight:** '{top_cat['category']}' has the highest average order value (${top_cat['sales']:,.2f}).")
    else:
        st.info("No category data available.")

# --- Popular Category ---
with tabs[4]:
    category_count = df_filtered['category'].value_counts().reset_index()
    category_count.columns = ['category', 'count']
    fig5 = px.bar(
        category_count,
        x='count',
        y='category',
        title='Popular Category',
        labels={'count': 'Count', 'category': 'Category'},
        color='category',
        text_auto='.2s',
    )
    fig5.update_layout(showlegend=False, xaxis_title='Count', yaxis_title='Category', autosize=True)
    fig5.update_traces(textfont_size=12, textposition="outside", cliponaxis=False)
    st.plotly_chart(fig5, use_container_width=True)
    # Insight for Popular Category
    if not category_count.empty:
        top_cat = category_count.iloc[0]
        st.info(f"**Insight:** '{top_cat['category']}' is the most frequently purchased category ({top_cat['count']} orders).")
    else:
        st.info("No category count data available.")

# --- Peak Hour ---
with tabs[5]:
    order_per_hour = df_filtered.groupby('hour')['id'].count().reset_index()
    order_per_hour.rename(columns={'id': 'count_of_orders'}, inplace=True)
    peak_hour = order_per_hour.loc[order_per_hour['count_of_orders'].idxmax(), 'hour'] if not order_per_hour.empty else None
    colors = ["#ffd700" if h == peak_hour else "#1f77b4" for h in order_per_hour['hour']]
    fig6 = px.bar(
        order_per_hour,
        x='hour',
        y='count_of_orders',
        title='Peak Hour',
        labels={'hour': 'Hour of Day', 'count_of_orders': 'Number of Orders'},
        text_auto='.2s',
        color_discrete_sequence=colors
    )
    fig6.update_traces(textfont_size=12, textposition="outside", marker_line_width=1.5)
    fig6.update_layout(
        showlegend=False,
        xaxis_title='Hour of Day',
        yaxis_title='Number of Orders',
        autosize=True,
        xaxis=dict(dtick=1),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    if peak_hour is not None:
        fig6.add_vline(x=peak_hour, line_dash="dash", line_color="#ffd700", annotation_text=f"Peak: {peak_hour}:00", annotation_position="top right")
    st.plotly_chart(fig6, use_container_width=True)
    # Insight for Peak Hour
    if not order_per_hour.empty and peak_hour is not None:
        peak_orders = order_per_hour.loc[order_per_hour['hour'] == peak_hour, 'count_of_orders'].values[0]
        st.info(f"**Insight:** Most orders are placed at {peak_hour}:00 ({peak_orders} orders). Consider staffing accordingly.")
    else:
        st.info("No hourly order data available.")

# --- Peak Day ---
with tabs[6]:
    weekdays_order = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    weekday_order_counts = df_filtered['weekday'].value_counts().reindex(weekdays_order).reset_index()
    weekday_order_counts.columns = ['weekday', 'count_of_orders']
    fig7 = px.bar(
        weekday_order_counts,
        x='weekday',
        y='count_of_orders',
        title='Peak Day',
        labels={'weekday': 'Weekday', 'count_of_orders': 'Count of Orders'},
        color='weekday',
        text_auto='.2s',
    )
    fig7.update_layout(showlegend=False, xaxis_title='Weekday', yaxis_title='Count of Orders', autosize=True)
    fig7.update_traces(textfont_size=12, textposition="outside", cliponaxis=False)
    st.plotly_chart(fig7, use_container_width=True)
    # Insight for Peak Day
    if not weekday_order_counts.empty and weekday_order_counts['count_of_orders'].max() > 0:
        peak_day = weekday_order_counts.loc[weekday_order_counts['count_of_orders'].idxmax()]
        st.info(f"**Insight:** {peak_day['weekday']} is the busiest day with {peak_day['count_of_orders']} orders.")
    else:
        st.info("No weekday order data available.")

# --- Coffee Types ---
with tabs[7]:
    coffee_type = df_filtered[df_filtered['category'] == 'Coffee'][['product']]
    coffee_type_count = coffee_type['product'].value_counts().reset_index()
    coffee_type_count.columns = ['product', 'count']
    fig8 = px.pie(
        coffee_type_count,
        names='product',
        values='count',
        title='Order Distribution by Coffee Type',
        labels={'sales': 'Sales', 'location': 'Location', 'product': 'Product', 'count': 'Order Count'},
        color='product',
        hole=0.4
    )
    fig8.update_traces(textinfo='percent+label', textfont_size=12)
    fig8.update_layout(legend_title_text='Product', autosize=True)
    st.plotly_chart(fig8, use_container_width=True)
    # Insight for Coffee Types
    if not coffee_type_count.empty:
        top_coffee = coffee_type_count.iloc[0]
        st.info(f"**Insight:** '{top_coffee['product']}' is the most popular coffee type with {top_coffee['count']} orders.")
    else:
        st.info("No coffee type data available.")

# --- Data Table & Download ---
with tabs[8]:
    st.dataframe(df_filtered)
    csv = df_filtered.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download filtered data as CSV",
        data=csv,
        file_name='filtered_coffee_sales.csv',
        mime='text/csv',
    )

# --- Advanced Feature: Custom Query (SQL) ---
st.sidebar.markdown("---")
st.sidebar.subheader("Custom Data Query (SQL)")
query = st.sidebar.text_area(
    "Enter a pandasql query (e.g., SELECT location, SUM(sales) as total_sales FROM df_filtered GROUP BY location)",
    height=80
)
if query:
    try:
        import pandasql as psql
        result = psql.sqldf(query, locals())
        st.write("Query Result:")
        st.dataframe(result)
    except Exception as e:
        st.error(f"Query error: {e}")

# --- Advanced Feature: Download Visualizations ---
with st.sidebar.expander("Download Visualizations", expanded=False):
    st.write("Download any chart as PNG:")
    st.info("Right-click on any chart and select 'Save image as...' to download.")

# --- Advanced Feature: Outlier Detection (Z-score) ---
with st.sidebar.expander("Outlier Detection", expanded=False):
    st.write("Detect outliers in sales using Z-score:")
    if not df_filtered.empty:
        import numpy as np
        sales = df_filtered['sales']
        z_scores = (sales - sales.mean()) / sales.std()
        outliers = df_filtered[np.abs(z_scores) > 3]
        st.write(f"Number of outlier transactions: {len(outliers)}")
        if not outliers.empty:
            st.dataframe(outliers[['id', 'date', 'location', 'sales']])
        else:
            st.info("No significant outliers detected.")
    else:
        st.info("No data to analyze for outliers.")

# --- Advanced Feature: Interactive Drilldown by Product ---
with st.sidebar.expander("Drilldown: Product Details", expanded=False):
    products = df_filtered['product'].dropna().unique().tolist()
    if products:
        selected_product = st.selectbox("Select a product to drill down:", options=products)
        if selected_product:
            product_df = df_filtered[df_filtered['product'] == selected_product]
            st.write(f"Sales trend for {selected_product}")
            if not product_df.empty:
                fig_prod = px.line(product_df, x='date', y='sales', title=f'Sales Trend: {selected_product}')
                st.plotly_chart(fig_prod, use_container_width=True)
                st.write(product_df[['date', 'location', 'sales', 'quantity']].sort_values('date', ascending=False))
            else:
                st.info("No data for selected product.")
    else:
        st.info("No products available for drilldown.")

# --- Advanced Feature: User Feedback ---
with st.sidebar.expander("Feedback", expanded=False):
    st.write("We value your feedback!")
    feedback = st.text_area("Share your suggestions or issues:")
    if st.button("Submit Feedback"):
        if feedback.strip():
            st.success("Thank you for your feedback!")
        else:
            st.warning("Please enter your feedback before submitting.")
