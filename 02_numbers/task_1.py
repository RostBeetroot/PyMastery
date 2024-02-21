def calculate_profit(total_sales):
    profit_percentage = 0.23
    profit = total_sales * profit_percentage
    return profit


total_sales = float(input("Enter total sales: "))
profit = calculate_profit(total_sales)
print(f"The profit is: {profit}")
