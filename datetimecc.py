#datetimecc.py

from datetime import datetime

my_datetime = datetime.now()
my_day = datetime.today()

# %Y = Year
# %m = Month
# %d = Day
# %H = Hour
# %M = Minute
# %S = Second

print(my_datetime)

print(f'Year:{my_day.year}')
print(f'Month:{my_day.month}')
print(f'Day:{my_day.day}')

my_string = my_day.strftime('%d/%m/%Y')
print(f'Formato LATAM: {my_string} ')
my_string = my_day.strftime('%m/%d/%Y')
print(f'Formato USA: {my_string} ')
my_string = my_day.strftime('Estamos en el año %Y')
print(f'Formato random: {my_string} ')