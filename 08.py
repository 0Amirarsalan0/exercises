num1 = float(input('inter first number: '))
num2 = float(input('inter second number: '))
num3 = float(input('inter third number: '))
if num1>num2 and num1>num3 and num2>num3 :
    print( num3 , num2 , num1)
elif num2>num1 and num2>num3 and num1>num3 :
    print( num3 , num1 , num2)
elif num3>num2 and num3>num1 and num2>num1 :
    print( num1 , num2 , num3)
