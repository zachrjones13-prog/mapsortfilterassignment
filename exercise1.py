prices = [25.00, 50.00, 75.00, 100.00, 150.00]

def discount(prices):
    return prices * 0.8


result = list(map(discount, prices))


print(prices)
print(result)