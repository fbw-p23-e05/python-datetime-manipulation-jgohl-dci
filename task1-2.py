import datetime as dt

current_datetime = dt.datetime.now()
print("Today:", current_datetime.strftime("%Y/%m/%d"))
result = current_datetime - dt.timedelta(days = 15)
print("Today -15 days:", result.strftime("%Y/%m/%d"))
result = current_datetime + dt.timedelta(days = 7)
print("Today +7 days:", result.strftime("%Y/%m/%d"))