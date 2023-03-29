from budget_app.core import Category, create_spend_chart
import unittest


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


class UnitTests(unittest.TestCase):
    def setUp(self):
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

        self.food = food
        self.auto = auto
        self.study = study
        self.clothing = clothing

    def test_category_class(self):
        result = str(self.food)
        expected = FOOD_CHECK
        self.assertEqual(result, expected)

        result = str(self.auto)
        expected = AUTO_CHECK
        self.assertEqual(result, expected)

        result = str(self.study)
        expected = STUDY_CHECK
        self.assertEqual(result, expected)

        result = str(self.clothing)
        expected = CLOTHING_CHECK
        self.assertEqual(result, expected)

    def test_create_spend_chart(self):
        categories = [self.food, self.auto, self.study, self.clothing]
        result = create_spend_chart(categories)
        expected = SPEND_CHART
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
