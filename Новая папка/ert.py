def apply_discounts(products, stocks):
    ls_stocks = list(stocks.keys())
    ls_products = list(products.keys())
    
    for stock in ls_stocks:
        print(stock)
        if stock in ls_products:
            
            procent = int(stocks[stock].replace('%', '')) / 100
            products[stock] = round((products[stock] - products[stock] * procent), 2)
    return products


print(apply_discounts(products = {'Oranges (packaged)': 114.99, 'Candy (Rotfront)': 280.0, 'Boiled sausage': 199.99, 'Juice J7 (orange)': 119.99, 'Trout (Seven Seas)': 399.99}, stocks = {'Oranges (packaged)': '15%', 'Boiled sausage': '10%', 'Candy (Rotfront)': '50%', 'Diapers': '10%'}))

a = {'Oranges (packaged)': 97.74, 'Candy (Rotfront)': 140.0, 'Boiled sausage': 179.99, 'Juice J7 (orange)': 119.99, 'Trout (Seven Seas)': 399.99}
print(a)