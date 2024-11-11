from flask import Flask, request, jsonify
import requests
import json

olx_url = 'https://www.olx.ro/oferte/q-apartament-2-camere/?page=1'
parser_url = 'http://127.0.0.1:5001/'

app = Flask(__name__)

@app.route('/get_page', methods=['POST'])
def get_storia_page():
    req = request.json
    page_nr = req['page']

    page = requests.get(olx_url + str(page_nr))

    req = requests.post(parser_url + 'parse', json=page.text)
    
    return jsonify({"msg": "Page was scraped!"})

@app.route('/start_scraping', methods=['GET'])
def start_scraping():
    for i in range(1, 20):
        try:
            req = requests.get(olx_url + str(i))
        except Exception as e:
            print(e)
            return jsonify({"msg": "Error while scraping!"})

        res_parser = requests.post(parser_url + 'parse', json=req.text)
        print(res_parser.json())

    return jsonify({"msg": "Scraping finished!"})


app.run(port=5000)