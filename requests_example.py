import requests

url = 'https://www.youtube.com'

req = requests.get(url)

print(req.status_code)
print("")
print(req.text)
print("")
print(req.headers)

file = open("youtube.html", "w")
file.write(req.text)