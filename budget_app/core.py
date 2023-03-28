CHECK_LENGTH = 30
CHECK_TITLE_FILL = "*"
SPEND_CHART_FILL = 'о'


class Category:
    def __repr__(self):
        check = ""
        title = self.category_name.center(
            CHECK_LENGTH, CHECK_TITLE_FILL
        ) + "\n"

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

cc.withdraw(45, 'cool shirt')

ccc = Category('Auto')
ccc.deposit(30, 'initial deposit')
ccc.withdraw(10, 'seats')

# print(c)
# print(cc)
# print(ccc)


def create_spend_chart(categories):
    title = "Percentage spent by category"
    spend_chart = [title]
    spent_dict = {}
    for category in categories:
        name = category.category_name
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += item["amount"]

        budget = category.get_balance() + abs(spent)
        spent_in_percentage = round((abs(spent) * 100) / budget, -1)
        spent_dict[name] = int(spent_in_percentage)

    for percent in range(100, -1, -10):
        line = f"{str(percent).rjust(3)}| "
        for key in spent_dict.keys():
            line += SPEND_CHART_FILL if spent_dict[key] >= percent else " "
            line += "  "
        spend_chart.append(line)
    borderline_length = 3 * len(spent_dict) + 1
    borderline = "    " + "-" * borderline_length
    spend_chart.append(borderline)

    names = [name for name in spent_dict.keys()]
    for i in range(max(map(len, names))):
        line = "     "
        for name in names:
            line += (f"{name[i]}" if len(name) > i else " ") + "  "
        spend_chart.append(line)

    return '\n'.join(spend_chart)


print(create_spend_chart([c, cc, ccc]))
