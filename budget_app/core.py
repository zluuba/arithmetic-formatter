CHECK_LENGTH = 30
FILL = "*"


class Category:
    def __repr__(self):
        check = ""
        title = self.category_name.center(CHECK_LENGTH, FILL) + "\n"

        for item in self.ledger:
            description = item["description"]
            amount = f"{item['amount']:.2f}"

            max_length = CHECK_LENGTH - (len(amount) + 1)
            if len(description) > max_length:
                description = description[:max_length]

            check += description + amount.rjust(
                CHECK_LENGTH - len(description)
            ) + "\n"

        total = f"Total: {self.get_balance():.2f}"
        return title + check + total

    def __init__(self, category_name):
        self.category_name = category_name
        self.ledger = []

    def deposit(self, amount, description=""):
        deposit = {"amount": amount, "description": description}
        self.ledger.append(deposit)

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            deposit = {"amount": -amount, "description": description}
            self.ledger.append(deposit)
            return True
        return False

    def transfer(self, amount, category):
        withdraw_description = f"Transfer to {category.category_name}"
        deposit_description = f"Transfer from {self.category_name}"

        if self.check_funds(amount):
            self.withdraw(amount, withdraw_description)
            category.deposit(amount, deposit_description)
            return True
        return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def check_funds(self, amount):
        balance = self.get_balance()
        if balance > amount:
            return True
        return False


c = Category('Food')
cc = Category('Clothing')

c.deposit(1000, 'initial deposit')
c.withdraw(10.15, 'groceries')
c.withdraw(15.89, 'restaurant and more food')
c.transfer(50.00, cc)

ccc = Category('Auto')
ccc.deposit(30, 'initial deposit')
ccc.withdraw(10, 'seats')

# print(c)
# print(cc)
# print(ccc)


def create_spend_chart(categories):
    for category in categories:
        print(category.category_name)
