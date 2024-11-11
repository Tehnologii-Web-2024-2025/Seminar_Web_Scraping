from flask import Flask, request, jsonify
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/parse', methods=['POST'])
def parse():
    data = request.json
    soup = BeautifulSoup(data, 'html.parser')
    print(soup.prettify())

    with open('page.html', 'w') as file:
        file.write(soup.prettify())

    return jsonify({'msg': "Page was parsed!"})
    
app.run(port=5001)