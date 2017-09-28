from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def index():
	return render_template('home.html')

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

if __name__ == "__main__":
	app.run(host='127.0.0.1')