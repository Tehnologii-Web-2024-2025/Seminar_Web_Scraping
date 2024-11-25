import flask
import json

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return {"msg": "Hello world!"}

@app.route('/user', methods=['GET'])
def user(): 
    return {
        "name": "Ion",
        "age": 20,
        "email": "ionionescu@gmail.com"
    }

@app.route('/set_user', methods=['POST'])
def set_user():
    req = flask.request.json
    print(req)
    req = json.loads(req)
    if(req['name'] == None):
        return {"msg": "Name required!"}
    
    if(req['age'] > 18):
        return {"msg": "Adult user created!"}
    else:
        return {"msg": "Minor user created!"}
    # return "Ceva!"
app.run(port=5000)
