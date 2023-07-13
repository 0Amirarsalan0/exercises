height = float(input('inter your height in meters:'))
weight = float(input('inter your weight:'))
bmi =weight/height**2
if bmi<18.5:
    print('your bmi is',bmi ,'\nyou are underweight')
elif bmi>=18.5 and bmi<=24.9 :
    print('your bmi is',bmi,'\nyour height and weight are normal')
elif bmi>=25 and bmi<=29.9:
    print('your bmi is',bmi,'\nyou are overweight')
elif bmi>=30:
    print('your bmi is',bmi,'\nyou are fat')
