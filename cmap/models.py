from datetime import datetime

# 1. Creating dictionary for all application headers
applicationHeaders = {
    'applicationName': 'CMAP',
    'titleHomePage': 'CMAP: Hyundai Trans Kazakhstan',
    'footer': '©2024 Hyundai Trans Kazakhstan | Almaty | All Rights Reserved'
}

# 2. Return current time
weekDays = {
   0: 'Monday',
   1: 'Tuesday',
   2: 'Wednesday',
   3: 'Thursday',
   4: 'Friday',
   5: 'Saturday',
   6: 'Sunday'
}
def get_current_time():
  current_time = datetime.now()
  # for week days:
  weekDayn = current_time.weekday()
  weekDay = ""
  for day in weekDays:
    if(day == weekDayn):
      weekDay = weekDays[day]
  # for minutes:
  minutes = current_time.minute;
  if(minutes < 10):
    minutes = '0' + str(minutes);
  else:
    minutes = str(minutes)
  return (weekDay + ", " + current_time.strftime("%d.%m.%Y")  + ", " + str(current_time.hour+5) + ':' + minutes)
  

a = get_current_time()
print(a)