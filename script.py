import os

var = 15

def foo():
    print("foo")

if var > 5: 
    print("da")

file = open("ceva.txt", "w")
file.write(str(var))

foo()