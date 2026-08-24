#List
numbers = [1, 2, 3, 4]
names = ["Alice", "Bob"]
mixed = [1, "hello", True, 3.5]
#Square numbers in range
squares = [x * x for x in range(6)]
print(squares)
#Upper case 
names = ["alice", "bob", "charlie"]
upper_names = [name.upper() for name in names]
print(upper_names)
#
products = ["laptop", "phone", "tablet", "monitor"]
upper_products = [p.upper() for p in products]
#List 2: Prices (numbers)
prices = [1000, 800, 450, 300]
discounted = [price * 0.9 for price in prices]
#List 3: Stock status (boolean)
in_stock = [True, False, True, False]
#Get indexes of products in stock
available = [i for i, stock in enumerate(in_stock) if stock]
#List 4: Product info as tuples
product_info = [("Laptop", 1000), ("Phone", 800), ("Tablet",
450)]
#Get names of products with price over 700
expensive = [name for name, price in product_info if price >
700]
#List 5: List of dictionaries
products_data = [
{"name": "Laptop", "price": 1000, "stock": 3},
{"name": "Phone", "price": 800, "stock": 0},
{"name": "Tablet", "price": 450, "stock": 5}
]
#Get available product names
available_names = [p["name"] for p in products_data if
p["stock"] > 0]
#Get discounted prices for products in stock
discounted_products = [{p["name"]: p["price"] * 0.9} for p in
products_data if p["stock"] > 0]
