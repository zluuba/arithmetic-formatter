from budget_app.core import Category, create_spend_chart


FOOD_CHECK = """*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96"""

AUTO_CHECK = """*************Auto*************
initial deposit          30.00
seats                   -10.00
Total: 20.00"""

STUDY_CHECK = """************Study*************
fellowship               50.00
office stuff            -42.00
Total: 8.00"""

CLOTHING_CHECK = """***********Clothing***********
Transfer from Food       50.00
cool shirt              -45.00
Total: 5.00"""

SPEND_CHART = """Percentage spent by category
100|             
 90|          о  
 80|       о  о  
 70|       о  о  
 60|       о  о  
 50|       о  о  
 40|       о  о  
 30|    о  о  о  
 20|    о  о  о  
 10| о  о  о  о  
  0| о  о  о  о  
    -------------
     F  A  S  C  
     o  u  t  l  
     o  t  u  o  
     d  o  d  t  
           y  h  
              i  
              n  
              g  """


def get_prepared_data():
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

    return food, auto, study, clothing


def test_category_class():
    food, auto, study, clothing = get_prepared_data()
    assert f"{food}" == FOOD_CHECK
    assert f"{auto}" == AUTO_CHECK
    assert f"{study}" == STUDY_CHECK
    assert f"{clothing}" == CLOTHING_CHECK


def test_create_spend_chart():
    categories = get_prepared_data()
    assert create_spend_chart(categories) == SPEND_CHART
