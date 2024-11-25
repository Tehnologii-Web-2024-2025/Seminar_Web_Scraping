from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
from datetime import datetime
import json

app = Flask(__name__)

@app.route('/parse', methods=['POST'])
def parse():
    data = request.json
    soup = BeautifulSoup(data, 'html.parser')

    with open('page.html', 'w') as file:
        file.write(soup.prettify())

    # title: class="css-1s3qyje"
    # price: class="css-13afqrm"

    titles = soup.find_all('h4', class_='css-1s3qyje')
    prices = soup.find_all('span', class_='css-13afqrm')

    send_data = json.dumps({"titles": [title.text for title in titles], "prices": [price.text for price in prices]})
    
    with open(f'parsed_data_{datetime.now()}.json', 'w') as file:
        file.write(send_data)

    # requests.post('http://127.0.0.1:3000', headers={'Content-Type': 'application/json'}, data=send_data)

    return jsonify({'msg': "Page was parsed!"})

app.run(port=5001)