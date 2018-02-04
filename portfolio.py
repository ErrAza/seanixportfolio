#!/usr/bin/env python
import sys
import requests
import json

sys.dont_write_bytecode = True

from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)

node_account = "xrb_31rgf5n8om6pja6y6xfcrq8f6j3rsq546ym9fmd3izoesjqw5ytimtbpdt9y"
node_wallet = "725328BD21A7E61081AD7EFA1B07B40B91B6502DE699F1B5B1D5149286DB1793"
personal_address = "xrb_1ny416pcmkzx5d3m8z49o7qetx7d9zyo97jr85zi5sbfx7szarohp1uek83p"

data = '{ "action": "block_count" }'
peers = '{ "action": "peers" }'
accountbalance = '{ "action": "account_balance", "account": "xrb_1ny416pcmkzx5d3m8z49o7qetx7d9zyo97jr85zi5sbfx7szarohp1uek83p" }'

@app.route("/")
def index():
	return render_template('home.html')

def ConvertFromRaw(amount):
	data ={}
	data['action'] = 'rai_from_raw'
	data['amount'] = amount
	json_string = json.dumps(data)
	response = requests.post('http://[::1]:7076', data=json_string)
	json_response = json.loads(response.text)
	return str(int(json_response["amount"]) / 1000000)

def GetBalance(address):
	data ={}
	data['action'] = 'account_balance'
	data['account'] = address
	json_string = json.dumps(data)
	response = requests.post('http://[::1]:7076', data=json_string)
	if response.status_code != 200:
		return "Cannot Find Account: " + address 

	json_response = json.loads(response.text)
	return ConvertFromRaw(json_response["balance"]) + " XRB"

@app.route("/nanobalance")
def nanobalance():
	address = request.args.get('address')
	return GetBalance(address)

@app.route("/nano")
def nano():
        blockcountresponse = requests.post('http://[::1]:7076', data=data)
        peersresponse = requests.post('http://[::1]:7076', data=peers)
        accountresponse = requests.post('http://[::1]:7076', data=accountbalance)
        c = json.loads(blockcountresponse.text)
        d = json.loads(peersresponse.text)
        e = json.loads(accountresponse.text)
        _blockCount = c["count"]
        _uncheckedBlocks = c["unchecked"]
        _peerCount = str(len(d["peers"]))
        _balance = ConvertFromRaw(e["balance"]) + " XRB"
        _pending = e["pending"]
        return render_template('nano.html', blockCount=_blockCount, uncheckedBlocks=_uncheckedBlocks, peerCount=_peerCount, balance=_balance, pending=_pending)

@app.route("/barblitz")
def barblitz():
	return render_template('barblitz.html')

@app.route("/eishhappens")
def eishhappens():
	return render_template('eishhappens.html')

@app.route("/mvar")
def mvar():
	return render_template('mvar.html')

@app.route("/sidehustle")
def sidehustle():
	return render_template('sidehustle.html')

@app.route("/superanimals")
def superanimals():
	return render_template('superanimals.html')

@app.route("/swipa")
def swipa():
	return render_template('swipa.html')

@app.route("/astudioclones")
def astudioclones():
	return render_template('astudioclones.html')

@app.route("/session")
def session():
	return render_template('session.html')

@app.route("/openweather")
def openweather():
	return render_template('openweather.html')

@app.route("/stardetect")
def stardetect():
	return render_template('stardetect.html')

@app.route("/permissiongranter")
def permissiongranter():
	return render_template('permissiongranter.html')

@app.route("/seanix")
def seanix():
	return render_template('seanix.html')

@app.route("/aboutme")
def aboutme():
	return render_template('aboutme.html')

@app.route("/contact")
def contact():
	return render_template('contact.html')

if __name__ == "__main__":
	app.run(host='0.0.0.0')
