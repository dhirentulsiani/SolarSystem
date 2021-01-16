import datetime

a = datetime.datetime(2021,1,16)
interval = (0.001 * 24 * 300) * 60
print(432 / 60)
print(interval)
intI = int(interval)
b = datetime.timedelta(hours=7, minutes=12)
print(a)
for i in range(1000):
    a = a + b
print(a.strftime('%Y-%m-%d'))