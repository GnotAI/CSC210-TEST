import matplotlib.pyplot as plt
import pandas as pd

# Sample data creation
df = pd.read_csv('car_sales.csv')

# --- Chart 1: Bar chart of Total Units Sold by Continent ---
plt.figure(figsize=(10, 6))
units_by_continent = df.groupby('Continent')['Units_Sold'].sum().sort_values(ascending=False)
units_by_continent.plot(kind='bar', color='skyblue')
plt.title('Total Units Sold by Continent')
plt.xlabel('Continent')
plt.ylabel('Total Units Sold')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('units_sold_by_continent_bar_chart.png')
plt.show()

# --- Chart 2: Pie chart of Percentage Revenue by Brand ---
plt.figure(figsize=(8, 8))
revenue_by_brand = df.groupby('Brand')['Revenue'].sum()
plt.pie(revenue_by_brand, labels=revenue_by_brand.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
plt.title('Percentage of Revenue by Brand')
plt.tight_layout()
plt.savefig('revenue_by_brand_pie_chart.png')
plt.show()

# --- Chart 3: Scatter plot of Units Sold vs. Unit Price ---
plt.figure(figsize=(10, 6))
plt.scatter(df['Unit_Price'], df['Units_Sold'], c=df['Discount'], cmap='viridis', s=df['Revenue']/50)
plt.title('Units Sold vs. Unit Price (Point Size by Revenue, Color by Discount)')
plt.xlabel('Unit Price')
plt.ylabel('Units Sold')
cbar = plt.colorbar()
cbar.set_label('Discount')
plt.tight_layout()
plt.savefig('units_sold_vs_unit_price_scatter_plot.png')
plt.show()

# --- Chart 4: Line chart of Average Revenue by Sales Channel ---
plt.figure(figsize=(10, 6))
avg_revenue_by_channel = df.groupby('Sales_Channel')['Revenue'].mean().sort_index()
avg_revenue_by_channel.plot(kind='line', marker='o', color='green')
plt.title('Average Revenue by Sales Channel')
plt.xlabel('Sales Channel')
plt.ylabel('Average Revenue')
plt.xticks(rotation=45)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.savefig('avg_revenue_by_sales_channel_line_chart.png')
plt.show()

# --- Chart 5: Histogram of Revenue Distribution ---
plt.figure(figsize=(10, 6))
plt.hist(df['Revenue'], bins=5, color='coral', edgecolor='black')
plt.title('Distribution of Revenue')
plt.xlabel('Revenue')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('revenue_distribution_histogram.png')
plt.show()

# --- Chart 6: Stacked Bar Chart of Units Sold by Continent and Sales Channel ---
plt.figure(figsize=(10, 6))
stacked_data = df.groupby(['Continent', 'Sales_Channel'])['Units_Sold'].sum().unstack()
stacked_data.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Units Sold by Continent and Sales Channel')
plt.xlabel('Continent')
plt.ylabel('Total Units Sold')
plt.xticks(rotation=45)
plt.legend(title='Sales Channel')
plt.tight_layout()
plt.savefig('units_sold_by_continent_and_channel_stacked_bar_chart.png')
plt.show()

# --- Chart 7: Horizontal Bar Chart of Total Discount by Brand ---
plt.figure(figsize=(10, 6))
discount_by_brand = df.groupby('Brand')['Discount'].sum().sort_values()
discount_by_brand.plot(kind='barh', color='purple')
plt.title('Total Discount by Brand')
plt.xlabel('Total Discount')
plt.ylabel('Brand')
plt.tight_layout()
plt.savefig('total_discount_by_brand_horizontal_bar_chart.png')
plt.show()

# --- Chart 8: Area chart of Cumulative Revenue by Continent ---
plt.figure(figsize=(10, 6))
cumulative_revenue = df.groupby('Continent')['Revenue'].sum().sort_index()
cumulative_revenue.cumsum().plot(kind='area', color='teal', alpha=0.5)
plt.title('Cumulative Revenue by Continent')
plt.xlabel('Continent')
plt.ylabel('Cumulative Revenue')
plt.xticks(rotation=45)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.savefig('cumulative_revenue_area_chart.png')
plt.show()

# --- Chart 9: Grouped Bar Chart of Average Units Sold and Average Revenue by Sales Channel ---
plt.figure(figsize=(12, 7))
avg_data = df.groupby('Sales_Channel')[['Units_Sold', 'Revenue']].mean()

x = range(len(avg_data.index))
width = 0.35

plt.bar(x, avg_data['Units_Sold'], width, label='Average Units Sold', color='skyblue')
plt.bar([i + width for i in x], avg_data['Revenue'], width, label='Average Revenue', color='coral')

plt.title('Average Units Sold and Revenue by Sales Channel')
plt.xlabel('Sales Channel')
plt.ylabel('Value')
plt.xticks([i + width / 2 for i in x], avg_data.index, rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig('avg_units_sold_and_revenue_by_sales_channel_grouped_bar_chart.png')
plt.show()
