import datetime as dt

current_datetime = dt.datetime(2020, 1, 1)
result = current_datetime + dt.timedelta(days = 25)
print("Hello Friedrich, your rent of 300 € is due on ", result.strftime("%d %B, %Y"), ".", sep="")