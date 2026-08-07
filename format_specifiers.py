# format specifiers -> {value : flags} -> format a value based on what flags are inserted

price1 = 13000.23214
price2 = -32.124
price3 = 22.3433

print(f"Price 1 is: ${price1:.2f}") #display to certain number of decimal places
print(f"Price 2 is: ${price2:10}") #total of 10 spaces allocated to the output
print(f"Price 3 is: ${price3:09}") #total spaces (0 in place of empty spaces)
print(f"Price 1 is: ${price1:<10}") #left alligned
print(f"Price 2 is: ${price2:>10}") #right alligned
print(f"Price 3 is: ${price3:^10}") #center alligned
print(f"Price 1 is: ${price1:+}") #for positive value
print(f"Price 1 is: ${price1:,}") #1000s separator

#You can use them separately or combination of these, based on your condition/usage