
NID_no = "36302-9618965-9"

print(NID_no[2]) #prints a specific index
print(NID_no[3:4]) #prints from start to end as given -> start is inclusive, end is exclusive
print(NID_no[:4]) #always starts from first index up til mentioned index
print(NID_no[4:]) #from mentioned index till last of the string
print(NID_no[::2]) #prints every 2nd character of the string

#example

last_digits = NID_no[-4:]
print(f"XXXXX-XXXX{last_digits}")

backward = NID_no[::-1]
print(f"Backward NID no: {backward}")
