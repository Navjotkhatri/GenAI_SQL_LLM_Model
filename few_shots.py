few_shots=[
    {
        'Question' : "total unit sold for each product for first month of sale?",
        'SQLQuery' : "SELECT Product_Category,SUM(Quantity) AS Total_Units_Sold FROM sales WHERE Date BETWEEN '01-01-2023' AND '31-01-2023' GROUP BY Product_Category ORDER BY Total_Units_Sold DESC",
        'SQLResult': "Result of the SQL query",
        'Answer' : "'Clothing : 874' ,'Electronics : 838','Beauty : 758' "
    }
]