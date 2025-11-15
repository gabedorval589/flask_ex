from flask import Flask render_template

app = Flask(__main__)

@app.route("/")
def hello():
    return "this is amazing"

@app.route('main')
def home():
    return(render_template)('index.html')

app.run(host='0.0.0.0', port=5000)