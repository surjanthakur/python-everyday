from uuid import uuid4


class Product:
    def __init__(self, item: str, price: int):
        self.item = item
        self.price = price

    def __str__(self):
        return f"{self.item} is {self.price}rs"


class Order:
    def __init__(self, username: str):
        self.order_id = str(uuid4())
        self.order_by = username


class Cart:
    def __init__(self):
        self.__products = []

    def add_product(self, product: Product):
        self.__products.append(product)
        print("product added")

    def show_cart(self):
        return self.__products

    def clear_cart(self):
        self.__products.clear()
        print("cart is empty")


class Customer:
    def __init__(self, username: str):
        self.username = username
        self.cart = Cart()
        self.orders = []

    def checkout(self):
        order = Order(self.username)
        self.orders.append(order)
        self.cart.show_cart()
        print("order placed")
        self.cart.clear_cart()


customer = Customer("surjan")

prod1 = Product("mango", 450)

customer.cart.add_product(prod1)
for item in customer.cart.show_cart():
    print(item)

customer.checkout()
