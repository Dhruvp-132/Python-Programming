class Product:
    def __init__(self, product_id, name, description, price, quantity):
        
        self._product_id = product_id
        self._name = name
        self._description = description
        self._price = price
        self._quantity = quantity

    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        if isinstance(value, str):
            self._product_id = value
        else:
            print("Product ID must be a string.")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            print("Name must be a String")

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if isinstance(value, str):
            self._description = value
        else:
            print("Description must be a string.")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, (float, int)):
            self._price = value
        else:
            print("Price must be an integer or float")

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if isinstance(value, int):
            self._quantity = value
        else:
            print("Quantity must be an integer.")

    def display_product_info(self):
       
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")
        print(f"Price: ${self.price:.2f}")
        print(f"Quantity: {self.quantity}")


class ShoppingCart:
    
    def __init__(self):
       
        self.cart_items = []  

    def add_to_cart(self, product):
       
        self.cart_items.append(product)

    def remove_from_cart(self, product_id):
        
        for item in self.cart_items:
            if item.product_id == product_id:
                self.cart_items.remove(item)
                break

    def display_cart(self):
        """
        Display all products in the shopping cart.
        """
        if not self.cart_items:
            print("Your shopping cart is empty.")
        else:
            print("Shopping Cart:")
            for item in self.cart_items:
                item.display_product_info()



product1 = Product("1", "Product 1", "Description 1", 10, 1)
product2 = Product("2", "Product 2", "Description 2", 20.49, 1)
product3 = Product("3", "Product 3", "Description 3", 15.75, 1)

print("------------------------------------------------------------")
# Create a shopping cart
cart = ShoppingCart()
print("------------------------------------------------------------")
# Add products to the cart
cart.add_to_cart(product1)
cart.add_to_cart(product2)
cart.add_to_cart(product3)
print("------------------------------------------------------------")
# Display the cart contents
cart.display_cart()
print("------------------------------------------------------------")
# Remove a product from the cart
cart.remove_from_cart("1")
print("------------------------------------------------------------")
# Display the updated cart contents
cart.display_cart()
