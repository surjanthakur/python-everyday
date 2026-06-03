class FoodCafe:
    def __init__(self, name: str, items: list):
        self.name = name
        self.items = items
        self.__book_order()

    def __book_order(self):
        print(f"your order is placed {self.name} sir items are: {self.items}")

    def get_my_order(self):
        print(f"here is your order {self.name} :=> {self.items}")


u1 = FoodCafe("surjan", ["burger", "fries", "pizza", "beer"])

u1.get_my_order()
