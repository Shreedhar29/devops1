import re

name = input("Enter your name: ")
pattern = r"\w+"
value = re.search(pattern, name)
if value:
    print(value.group())
else:
    print("Sorry, you didn't enter a name")
