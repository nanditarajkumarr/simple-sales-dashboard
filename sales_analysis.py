import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="sale_db"
)

query = "SELECT * FROM raw_data"

df = pd.read_sql(query, conn)
print("data loaded")

#print(df.head())
#print(df.isnull().sum())

#created profit% column
#df["Profit%"]=(df["Profit"]/df["Sales"])*100
#print(df[["Sales","Profit","Profit%"]].head())

#create year column - date not in format mayb
#df["year"]=df["Date"].dt.year
#print(df[["Date","year"]].head())

#achievement percentage
#df["achievement%"]=((df["Sales"]/df["Target"])*100).round(2)
#print(df[["Sales","Target","achievement%"]].head())

#region sales
#region_sales=df.groupby("Region")["Sales"].sum()
#print(region_sales)

# region sales in bar chart
'''import matplotlib.pyplot as plt
region_sales=df.groupby("Region")["Sales"].sum()
region_sales.plot(kind="bar")
plt.title("TOTAL SALES BY REGION")
plt.xlabel("region")
plt.ylabel("sales")
plt.show() '''

#monthly sales trend
import matplotlib.pyplot as plt
monthly_sales = df.groupby("Month")["Sales"].sum()

monthly_sales.plot(kind="line")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

conn.close()