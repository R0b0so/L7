unit = int(input("how much is your eletricity consumption?"))
if unit < 50:
    print((unit * 2.60)+ 25)
elif unit >= 50 and unit < 100:
    print((unit * 3.25)+ 35)
elif unit >= 100 and unit < 200:
    print((unit * 5.26)+ 45)
elif unit >= 200:
    print((unit * 8.45)+ 75)