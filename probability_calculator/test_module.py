from probability_calculator.core import Hat, experiment
import unittest
import random


random.seed(1)


class UnitTests(unittest.TestCase):
    def test_hat_class(self):
        hat = Hat(red=4, green=3)
        result = sorted(hat.draw(2))
        expected = ["green", "red"]
        self.assertEqual(result, expected)

        hat = Hat(blue=2, black=3)
        result = hat.draw(10)
        expected = ["blue", "blue", "black", "black", "black"]
        self.assertEqual(result, expected)

    def test_experiment(self):
        hat = Hat(black=6, red=4, green=3)
        result = experiment(
            hat=hat, expected_balls={"red": 2, "green": 1},
            num_balls_drawn=5, num_experiments=100
        )
        expected = 0.45
        self.assertEqual(result, expected)

        hat = Hat(green=1, red=3, blue=10)
        result = experiment(
            hat=hat, expected_balls={"red": 1, "blue": 1},
            num_balls_drawn=4, num_experiments=500
        )
        expected = 0.664
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
