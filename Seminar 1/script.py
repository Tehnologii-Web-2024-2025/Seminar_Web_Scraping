import requests
import os

print("hello, world!")

res = requests.get("https://natureofcode.com/")

# file = open("index.html", "w")
# file.write(res.text)

print(res.headers)