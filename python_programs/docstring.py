# Docstring in Python

# Declaring Docstrings: The docstrings are declared using ”’triple single quotes”’ or 
#                       “””triple double quotes””” just below the class, method or function declaration. 
#                       All functions should have a docstring.

# Accessing Docstrings: The docstrings can be accessed using the __doc__ method of the object or using 
#                       the help function.

def func():
    """ Demonstrates triple double qoutes docstrings and does nothing really"""
    return None

if __name__ == "__main__":
    print("Using __doc__:")
    print(func.__doc__)

    print("Using help:")
    help(func)