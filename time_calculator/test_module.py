from time_calculator.core import add_time
import unittest


class UnitTests(unittest.TestCase):
    def test_add_time(self):
        result = add_time("3:00 PM", "3:10")
        expected = "6:10 PM"
        self.assertEqual(result, expected)

        result = add_time("11:30 AM", "2:32", "Monday")
        expected = "2:02 PM, Monday"
        self.assertEqual(result, expected)

        result = add_time("11:43 AM", "00:20")
        expected = "12:03 PM"
        self.assertEqual(result, expected)

        result = add_time("10:10 PM", "3:30")
        expected = "1:40 AM (next day)"
        self.assertEqual(result, expected)

        result = add_time("11:43 PM", "24:20", "tueSday")
        expected = "12:03 AM, Thursday (2 days later)"
        self.assertEqual(result, expected)

        result = add_time("6:30 PM", "205:12")
        expected = "7:42 AM (9 days later)"
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
