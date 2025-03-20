# ask the user for its full name in incorrect casing
user_name = str(input("\nEnter your full name: "))

# remove the spaces in the input
remove_space = user_name.strip()

# fix the casing
pascal_case = remove_space.title().replace(" ","")

# print the output
print(pascal_case)