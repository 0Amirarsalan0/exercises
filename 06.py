a = float(input('enter the grade of first student:'))
b = float(input('enter the grade of sec student:'))
c = float(input('enter the grade of third student:'))
gpa = (a+b+c)/3
if gpa>17 and gpa<=20:
    print('excellent')
elif gpa>=12 and gpa<=17:
    print('good')
else :
    print('rejected')