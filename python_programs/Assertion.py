# Assertion in Python.
"""
The assert keyword is used when debugging code.
The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError.
You can write a message to be written if the code returns False, check the example below.
"""

x = "hello"

# if the condition returns true , then noting happens:
assert x == "hello"
print("Passing the hello.")

# if the condition returns false , Assertion is raised:
assert x == "goodbye"
# The assert keyword is used when debugging code.
# The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError.
# You can write a message to be written if the code returns False, check the example below.

# Note : After asertion error next statement didn't execute

# -------------------------------------------------------------------------------------------
y = "hello"
# Write a message if the condition is False:
assert y == "good" , "x should be 'hello'"