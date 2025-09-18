#Retail Sales Insights with Pandas, SQLite, and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 
import sqlite3 


df=pd.read_csv(r"C:\Users\suvee\OneDrive\Desktop\project_ml_beginner\sales.csv")
conn = sqlite3.connect("sales.db")
cur = conn.cursor()

df.to_sql("sales", conn, if_exists = "replace", index=False)

#Total revenue by region
high_rev= "Select Region, SUM(QUANTITY*PRICE)AS REVENUE FROM SALES GROUP BY REGION"
df_rev = pd.read_sql_query(high_rev,conn)
plt.figure(figsize=(6,4))
sns.barplot(x="Region",y="REVENUE",data= df_rev,palette="coolwarm")
plt.title("Total Revenue by Region", fontsize=14,fontweight="bold")
plt.xlabel("Region",fontsize=12)
plt.ylabel("Revenue",fontsize=12)
plt.grid(axis="y",linestyle="--",alpha=0.7)
plt.show(block=True)

#Max quantity by region
high_quan= "SELECT REGION, MAX(QUANTITY) AS HIGH_QUANTITY  FROM SALES GROUP BY REGION"
df_quan=pd.read_sql_query(high_quan,conn)
plt.figure(figsize=(6,4))
sns.barplot(x="Region",y="HIGH_QUANTITY",data= df_quan,palette="Set2")
plt.title("Max Quantity Sold per region",fontsize=14,fontweight="bold")
plt.xlabel("Region",fontsize=12)
plt.ylabel("Quantity",fontsize=12)
plt.grid(axis="y",linestyle="--",alpha=0.7)
plt.show(block=True)

#Top 5 products by revenue
query3="SELECT PRODUCT, SUM(price) AS TOTAL_REVENUE FROM SALES GROUP BY PRODUCT ORDER BY TOTAL_REVENUE DESC LIMIT 5"
df_top=pd.read_sql_query(query3,conn)
plt.figure(figsize=(6,4))
sns.barplot(data= df_top, x="Product",y="TOTAL_REVENUE",palette="viridis")
plt.title("Top 5 products by revenue  ",fontweight="bold",fontsize=14)
plt.xlabel("Product",fontsize=12)
plt.ylabel("Revenue",fontsize=12)
plt.grid(axis="y",linestyle="--",alpha=0.7)
plt.show(block=True)

conn.close()