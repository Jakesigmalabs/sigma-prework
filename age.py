from datetime import date


def year_diff(d1, d2):
    day_diff = abs(d1-d2).days
    return (day_diff//365)


def main():
    year = int(input("Please list the year "))
    month = int(input("Please list the month (in digits) "))
    day = int(input("Please list the day (in digits) "))
    users_input = date(year, month, day)
    current_date = date.today()
    result = year_diff(users_input, current_date)
    print(result)


main()
