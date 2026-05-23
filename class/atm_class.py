class Atm:

    # ~ it's an constructor that execute's its value's automatically when the class object created
    def __init__(self, pin: str, balance: int):  # its a special method
        self.pin = pin
        self.balance = balance

    def check_balance(self, pin: str):
        if self.pin == pin:
            print(f"your amount is: {self.balance}")
        else:
            print("wrong pin")

    def set_pin(self, pin: str):
        if len(pin) <= 3 or len(pin) >= 1:
            self.pin = pin

    def add_amount(self, amount: int, pin: str):
        if amount > 0:
            if self.pin == pin:
                self.balance += amount
                print(
                    f"amount diposite successfully , now your curr balance is {self.balance}"
                )

    def debit_ammount(self, amount: int, pin: str):
        if amount > 0 or amount <= self.balance:
            if self.pin == pin:
                self.balance -= amount
                print(
                    f"amount debited successfully , now your curr balance is {self.balance}"
                )


# create default account with pin and the amount
my_account = Atm(pin="1234", balance=4000)

my_account.debit_ammount(amount=500, pin="1234")
