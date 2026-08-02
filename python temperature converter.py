# temperature converter (C -> F OR F -> C)

temp = float(input("Enter the temperature: "))
unit = input("Enter the unit of temperature: ")

if unit == "C":
    response = input("Do you want to convert your temperature into F? (Y/N) : ")
    if response == "Y" or response == "y":
        fahren_temp =  (temp * 9/5) + 32
        unit = "F"
        print(f"Your temperature is: {round(fahren_temp, 2)}{unit}")
    else:
        print("No convertion requested. Thank you!")
elif unit == "F":
    response = input("Do you want to convert your temperature into C? (Y/N) : ")
    if response == "Y" or response == "y":
        centi_temp =  (temp - 32) * 5/9
        unit = "F"
        print(f"Your temperature is: {round(centi_temp, 2)}{unit}")
    else:
        print("No convertion requested. Thank you!")
elif unit == "":
    print("ERROR! No unit entered.")
else:
    print(f"{unit} is not  valid unit.")