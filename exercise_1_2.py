import datetime
value = int(input("Введите количество секунд >>>"))

minutes = value // 60
seconds = value - minutes * 60
hours = minutes // 60
minutes = minutes - hours * 60
if seconds < 10:
    seconds = f"0{seconds}"
if minutes < 10:
    minutes = f"0{minutes}"
if hours < 10:
    hours = f"0{hours}"
print(f"{hours}:{minutes}:{seconds}")
print(str(datetime.timedelta(seconds=value)))