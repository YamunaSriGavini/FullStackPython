#To Create Class
class Product:
    platform = "Flipkart"
    def display_product(self):
        print("Displaying Product Details")

    def check_stock(self):
        print("Stock Available")
# create objects
class Product:
    platform = "Flipkart"
    laptop = Product()
    mobile = Product()
    headphones = Product()
# Accessing attributes
class Product:
    platform = "Flipkart"
    laptop = Product()
    print(laptop.platform)
#using methods,Instance method
class Product:
    def display_product(self):
        print("Displaying Product Details")
laptop = Product()
laptop.display_product()
# Class method
class Product:
    delivery_charge = 40
    @classmethod
    def update_delivery_charge(cls):
        cls.delivery_charge = 60
Product.update_delivery_charge()
print(Product.delivery_charge)
#Static Method
class Product:
    @staticmethod
    def free_delivery(price):
        return price >= 500
print(Product.free_delivery(800))
print(Product.free_delivery(300))