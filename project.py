import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


df = pd.read_excel('A:/power BI/python/Sales_Adhoc_Analysis_Data.xlsx')
df

df.info
print(df.isnull().sum())

#duplicate check
duplicate_rows = df[df.duplicated()]
print("Number of fully duplicated rows:", len(duplicate_rows))


#checking time frame of the data
df['Date'] = pd.to_datetime(df['Date'])
print(f"Date range: {df['Date'].min()} to {df['Date'].max()}")

#trend analysis
monthly_sales = df.groupby(df['Date'].dt.to_period('M'))['Revenue'].sum()
monthly_sales.plot(kind='line', title='Monthly Sales Trend', xlabel='Month', ylabel='Revenue', figsize=(10, 5))
plt.show()

# Sales by Region
revenue_region = df.groupby([df['Date'].dt.to_period('M'), 'Region'])['Revenue'].sum().sort_values(ascending=False).unstack()
revenue_region.plot(kind='bar', title='Total Revenue by Region')
plt.ylabel('Revenue')
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x * 1e-6:.0f}M'))
plt.xticks(rotation=00, ha='right')
plt.legend(title='Region', loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()

# Sales by Category
revenue_Category = df.groupby([df['Date'].dt.to_period('M'),'Category'])['Revenue'].sum().sort_values(ascending=False).unstack()
revenue_Category.plot(kind='line', title='Total Revenue by Category', figsize=(10, 5))
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x * 1e-6:.0f}M'))
plt.xticks(rotation=00, ha='right')
plt.legend(title='Category', loc='upper left', bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()

# Units Sold by Region
filtered_df = df[(df['Category'].isin(['Clothing', 'Electronics'])) & (df['Region'] == 'East')]
unit_sold_region = filtered_df.groupby([filtered_df['Date'].dt.to_period('M'), 'Category'])['Units_Sold'].sum().sort_values(ascending=False).unstack()
unit_sold_region.plot(kind='line', title='Total Units Sold by Category (East Region)', figsize=(10, 5))
plt.xticks(rotation=0, ha='right')
plt.legend(title='Category', loc='upper left', bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()

filtered_df = df[(df['Category'].isin(['Clothing', 'Electronics'])) & (df['Region'] == 'West')]
unit_sold_region = filtered_df.groupby([filtered_df['Date'].dt.to_period('M'), 'Category'])['Units_Sold'].sum().sort_values(ascending=False).unstack()
unit_sold_region.plot(kind='line', title='Total Units Sold by Category (East Region)', figsize=(10, 5))
plt.xticks(rotation=0, ha='right')
plt.legend(title='Category', loc='upper left', bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()

filtered_df = df[(df['Category'].isin(['Clothing', 'Electronics'])) & (df['Region'] == 'North')]
unit_sold_region = filtered_df.groupby([filtered_df['Date'].dt.to_period('M'), 'Category'])['Units_Sold'].sum().sort_values(ascending=False).unstack()
unit_sold_region.plot(kind='line', title='Total Units Sold by Category (East Region)', figsize=(10, 5))
plt.xticks(rotation=0, ha='right')
plt.legend(title='Category', loc='upper left', bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()

filtered_df = df[(df['Category'].isin(['Clothing', 'Electronics'])) & (df['Region'] == 'South')]
unit_sold_region = filtered_df.groupby([filtered_df['Date'].dt.to_period('M'), 'Category'])['Units_Sold'].sum().sort_values(ascending=False).unstack()
unit_sold_region.plot(kind='line', title='Total Units Sold by Category (East Region)', figsize=(10, 5))
plt.xticks(rotation=0, ha='right')
plt.legend(title='Category', loc='upper left', bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()

