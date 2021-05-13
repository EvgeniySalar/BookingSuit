from datetime import timedelta, datetime


def add_some_day():
    """
    this function determines the current day and returns the day after tomorrow
    :return: generate XPATH the day after tomorrow
    """

    day_today = datetime.now()
    print(day_today)
    add_days = timedelta(2)
    in_two_days = day_today + add_days
    make_str_new_day = in_two_days.strftime('%Y-%m-%d')
    return make_str_new_day
