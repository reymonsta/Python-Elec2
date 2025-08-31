# Python weight converter


weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K":
    weight *= 2.205
    unit = "Pounds"
    print(f"Your weight is: {round(weight, 1)} {unit}")
elif unit == "L":
    weight /= 2.205
    unit = "Kilograms"
    print(f"Your weight is: {round(weight, 1)} {unit}")
else:
    print(f"{unit} was not valid")

