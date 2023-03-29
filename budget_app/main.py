from budget_app.core import Category, create_spend_chart


def main():
    food = Category('Food')
    auto = Category('Auto')
    study = Category('Study')
    clothing = Category('Clothing')

    food.deposit(1000, 'initial deposit')
    food.withdraw(10.15, 'groceries')
    food.withdraw(15.89, 'restaurant and more food')
    food.transfer(50.00, clothing)

    auto.deposit(30, 'initial deposit')
    auto.withdraw(10, 'seats')

    study.deposit(50, 'fellowship')
    study.withdraw(42, 'office stuff')
    study.withdraw(100, 'OOP course')

    clothing.withdraw(45, 'cool shirt')

    print(food)
    print()
    print(create_spend_chart([food, auto, study, clothing]))


if __name__ == '__main__':
    main()
