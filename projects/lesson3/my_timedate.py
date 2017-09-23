
from datetime import datetime, date, timedelta
import locale
import calendar

locale.setlocale(locale.LC_TIME, "ru_RU.utf8")

dt_now = datetime.now()
dt_yesterday = datetime.now() - timedelta(days=1)
days_month_ago = calendar.monthrange(dt_now.year, dt_now.month - 1)
dt_month_ago = dt_now - timedelta(days=days_month_ago[1])

print(dt_now.strftime('%d %B %Y'))
print(dt_yesterday.strftime('%d %B %Y'))
print(dt_month_ago.strftime('%d %B %Y'))

date_string = '01/01/17 12:10:03.234567'
date_dt = datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')

print(date_dt)


# print(cal)
# print(dt_month_ago.strftime('%d %B %Y'))