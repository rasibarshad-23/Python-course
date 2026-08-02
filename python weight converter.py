#python weight converter (kg -> lbs OR lbs -> kg)

weight = float(input("Enter your weight: "))
unit = input("Enter the unit of yout weight: ")

if unit == "kg":
    response = input("Do you want to convert your weight into lbs? (Y/N) : ")
    if response == "Y" or response == "y":
        converted_weight =  weight * 2.205
        unit = "lbs"
        print(f"Your weight is: {round(converted_weight, 2)} {unit}")
    else:
        print("No convertion requested. Thank you!")
elif unit == "lbs":
    response = input("Do you want to convert your weight into kg? (Y/N) : ")
    if response == "Y" or response == "y":
        converted_weight =  weight * 0.4536
        unit = "kg"
        print(f"Your weight is: {round(converted_weight, 2)} {unit}")
    else:
        print("No convertion requested. Thank you!")
elif unit == "":
    print("ERROR! No unit entered.")
else:
    print(f"{unit} is not  valid unit.")