year = int(input('inter the year: '))
month = int(input('inter the month: '))
day = int(input('inter the day: '))
year2 = int(input('inter your birth year: '))
month2 = int(input('enter your birth month: '))
day2 = int(input('enter your birth day: '))
y = year-year2
m = month-month2
d = day-day2
tr = 30
if m<0 :
    m = m+12
    y = y-1
if m<=6 and m!=0 :
    tr = 31
if d<0 :
    d = d+tr
    m = m-1
print('year: ',y,'\nmonth: ',m,'\nday: ',d)
ds = 86400*d
x = tr*86400
ms = x*m
ys = (86400*365)*y
all_sec = ds+ms+ys
print('the seconds of your life are: ',all_sec)