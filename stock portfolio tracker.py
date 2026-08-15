stock_prices = {
    "AAPL":180,
    "TSLA":250,
    "GOOGL":150,
    "MSFT":400,
    "AMZN":180
}
total_investment = 0
print("==== stock portfolio tracker ====")
print("available stocks:",",". join(stock_prices.keys()))
while True:
    stock = input("\nenter stock name (or 'done' to finish):").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("stock not available.")
        continue
    quantity = int(input("enter quantity:"))
    investment = stock_prices[stock]* quantity
    total_investment += investment
    print("investment in", stock, "=",investment)
    print("\n===== portfolio summary =====")
    print("total investment: $",total_investment)
