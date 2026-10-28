products = [ 

    {"name": "Keyboard", "price": 45}, 

    {"name": "Monitor", "price": 180}, 

    {"name": "Mouse", "price": 25}, 

    {"name": "Headphones", "price": 75}, 

    {"name": "USB Drive", "price": 15}, 

    {"name": "Webcam", "price": 60} 

] 

prod_under_50 = list(filter(lambda products: products["price"] <= 50, products))

print(prod_under_50)

for product in prod_under_50:
    print(f'{product["name"]} - ${product["price"]}')
