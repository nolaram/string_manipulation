# ask user to input a complete statement
statement = str(input("\nEnter a complete statement: "))

# seperate the words
words = statement.split()

# count the number of words
word_count = len(words)

# print the output
print(word_count)