class Atm:
    def __init__(self, pin: str, balance: int):
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


my_account = Atm(pin="1234", balance=4000)

my_account.add_amount(amount=3400, pin="1234")
