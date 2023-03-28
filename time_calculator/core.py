from math import ceil

WEEK = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

AM = 'AM'
PM = 'PM'

MINUTES = 60
FULL_DAY = 24
HALF_DAY = 12


def get_result_time(meridiem, start, duration):
    start_hour, start_minute = start
    duration_hour, duration_minute = duration

    result_hour = start_hour + duration_hour
    result_minute = start_minute + duration_minute

    if result_minute >= MINUTES:
        added_hours = result_minute // MINUTES
        result_minute = result_minute % MINUTES
        result_hour += added_hours
    total_hours = result_hour

    if result_hour > 12:
        result_hour = result_hour % 12

    added_days = 0
    while total_hours >= 12:
        if meridiem == AM:
            meridiem = PM
        else:
            meridiem = AM
            added_days += 1
        total_hours -= 12

    if result_hour == 0:
        result_hour = 12

    return result_hour, result_minute, added_days, meridiem


def get_weekday(starting_day, added_days):
    starting_day = starting_day.lower()
    days = added_days + WEEK.index(starting_day)
    result_day = days % len(WEEK)
    result_day = WEEK[result_day]
    result_day = result_day.title()
    return f", {result_day}"


def get_days_count(added_days):
    if added_days == 1:
        return " (next day)"
    return f" ({added_days} days later)"


def add_time(start_time, duration_time, starting_day=None):
    time, meridiem = start_time.split()
    start_hour, start_minute = time.split(':')
    start = int(start_hour), int(start_minute)

    duration_hour, duration_minute = duration_time.split(':')
    duration = int(duration_hour), int(duration_minute)

    result_time = get_result_time(meridiem, start, duration)
    result_hour, result_minute, added_days, meridiem = result_time

    result = f"{result_hour}:{result_minute:02d} {meridiem}"

    if starting_day:
        result += get_weekday(starting_day, added_days)
    if added_days:
        result += get_days_count(added_days)

    return result
