# ask the user to input a number (0 - 1000)
number = input("\nEnter a number from 0 to 1000: ")

# print the output with zero's that fill it till it's six digits
six_digit = number.zfill(6)
print(six_digit)