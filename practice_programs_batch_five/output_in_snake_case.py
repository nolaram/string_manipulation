# ask user to input fullname in incorrect casing
user_name = str(input("Enter your fullname: "))

# convert the casing to lower case and replace the space with an underscore
snake_case = user_name.lower().replace(" ","_")

# print the output