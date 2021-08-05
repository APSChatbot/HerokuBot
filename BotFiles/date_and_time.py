from datetime import datetime
import pytz


def current_Datetime():
    current_time = datetime.now(pytz.timezone('Asia/Kolkata'))
    time = current_time.strftime('%H:%M:%S')
    year = current_time.year
    current_month = current_time.month
    months = ['None', 'January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    for month in months:
        month = months[current_month]
    date = current_time.day
    current_day = current_time.weekday()
    days = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']
    for day in days:
        day = days[current_day]
    return f'Current Date is: <br> {date}-{month}-{year} <break> Current Day is: <br> {day} <break> Current Time is: <br>{time}'
