#sql queries to ans few business question
#select first 2
#select * from raw_data limit 2;

#last 5
#select*from raw_data order by Units desc limit 5;

#total sales
#select sum(Sales) as total_sales from raw_data;

#total records
#select count(*) as total_records from raw_data;

#total profit
#select sum(profit) as total_profits from raw_data;

#total units sold
#select sum(units) as total_units from raw_data;

#sales by region
#select region,sum(sales) as total_sales from raw_data group by region order by total_sales desc;

#profit by region
#select region,sum(profit) as total_profit from raw_data group by region order by total_profit desc;

#top 10 customers
#select customer,sum(units) as total_units,sum(sales) as total_sales from raw_data group by customer order by total_sales desc limit 10; 

#best selling product
#select product,sum(units) as total_units from raw_data group by product order by total_units;

#sales by category
#select category,sum(sales) as TOT_sales from raw_data group by category order by tot_sales desc;

#monthly sales trend
#select month,sum(sales) as tot_sales from raw_data group by month order by tot_sales desc;
