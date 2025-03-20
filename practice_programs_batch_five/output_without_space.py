# ask user to input name with spaces in the beginning 
user_name = str(input("\nEnter your fullname: "))

# print the output without the spaces
remove_space = user_name.strip()
print (remove_space)