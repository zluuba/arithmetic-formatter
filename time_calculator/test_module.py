from time_calculator.core import add_time


def test_add_time():
    assert add_time("3:00 PM", "3:10") == "6:10 PM"
    assert add_time("11:30 AM", "2:32", "Monday") == "2:02 PM, Monday"
    assert add_time("11:43 AM", "00:20") == "12:03 PM"
    assert add_time("10:10 PM", "3:30") == "1:40 AM (next day)"
    assert add_time("11:43 PM", "24:20", "tueSday") == "12:03 AM, Thursday (2 days later)"
    assert add_time("6:30 PM", "205:12") == "7:42 AM (9 days later)"
