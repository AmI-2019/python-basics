# this is the hello world
print("Hello world")

"""
this is a multiline comment
this another line of the comment
"""
language_name = "Python"
version = '3.7.0'
introduced = 1991
is_awesome = True

another = 0o1234
# print(another)

# check the current type of the "language_name" variable
print(type(language_name))
# print(type(introduced))

# Strings
a_string = "I'm a string"
another_string = 'I\'m string, too'

a_very_long_string = """This is the first line.
This is the second line.
This is the third line.
"""

# If Statement
people = 20
cats = 30

if people < cats:
    print("Too many cats! We are doomed!")
elif people > cats:
    print("We are safe!")
else:
    print("We can't decide")

print("We are outside the if statement")
