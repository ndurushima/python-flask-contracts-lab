#!/usr/bin/env python3
import os
from flask import Flask, request, current_app, g, make_response

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]

customers = ["bob","bill","john","sarah"]

app = Flask(__name__)

@app.before_request
def app_path():
    g.path = os.path.abspath(os.getcwd())

@app.route('/')
def index():
    host = request.headers.get('Host')
    appname = current_app.name
    response_body = f'''
        <h1>The host for this page is {host}</h1>
        <h2>The name of this application is {appname}</h2>
        <h3>The path of this application on the user's device is {g.path}</h3>
    '''
    status_code = 200
    headers = {}
    return make_response(response_body, status_code, headers)

@app.route('/contract/<id>')
def get_contract(id):
    if id in contracts:
        return make_response(contracts, 200)
    else:
        return make_response({"error": "Contract not found"}, 404)

@app.route('/customer/<customer_name>')
def get_customer(customer_name):
    if customer_name in customers:
        return make_response({"customer": customer_name}, 200)
    else:
        return make_response({"error": "Customer not found"}, 404)
    
if __name__ == '__main__':
    app.run(port=5555, debug=True)
