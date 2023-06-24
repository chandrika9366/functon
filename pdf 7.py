# Q7.Write function bmi that calculates body mass index (bmi = weight / height2).
# if bmi <= 18.5 return "Underweight"
# if bmi <= 25.0 return "Normal"
# if bmi <= 30.0 return "Overweight"
# if bmi > 30 return "Obese"
def bmi():
    weight=int(input("enter weight"))
    height=int(input("enter height"))
    a=weight/height**2
    if a<=18.5:
        return "underweight"
    elif a<=25.0:
        return "normal"
    elif a<=30.0:
        return "overweight"
    elif a>30:
        return "obese"
print(bmi())                        