''' Answer Problem 1 here '''
from cs110 import expect, summarize

def add_hello_world(s: str)-> str:
    """
    Purpose: returns a string with "Hello world! " at the front of it
    Examples:
    add_hello_world("Good Morning") # "Hello world! Good Morning"
    add_hello_world("Python Programming") # "Hello world! Python Programming"
    add_hello_world("Welcome to coding") # "Hello world! Welcome to coding"
    """
    
    return "Hello world! " + s     #stub

# testing
expect(add_hello_world("Good Morning"), equals = "Hello world! Good Morning")
expect(add_hello_world("Python Programming"), equals = "Hello world! Python Programming")
expect(add_hello_world("Welcome to coding"), equals = "Hello world! Welcome to coding")
summarize()