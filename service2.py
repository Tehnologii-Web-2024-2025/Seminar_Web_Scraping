import requests 
import json
from flask import Flask, request, jsonify

url_service1 = 'http://127.0.0.1:5000/'

# def test_hello():
#     res = requests.get(url_service1)
#     data = res.json()

#     print(data["msg"])

# def test_user():
#     res = requests.get(url_service1 + 'user')
#     data = res.json()

#     print("Hello " + data["name"] + "!")
#     print(f"Hello {data['name']}!")

# def test_set_user(): 
#     user = {
#         "name": "Ana",
#         "age": 15,
#         "email": "anaanescu@gmail.com"
#     }

#     user = json.dumps(user)

#     req = requests.post(url_service1 + "set_user", json=user)
#     print(req.text)

# # test_hello()
# # test_user()
# test_set_user()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    res = requests.get(url_service1)
    data = res.json()
    data["msg2"] = "Hello from service2!"
    return jsonify(data)

app.run(port=5001)