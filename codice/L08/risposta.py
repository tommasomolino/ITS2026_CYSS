from flask import Flask, jsonify, render_template
from richiesta import lista

app = Flask(__name__)

@app.route('/api/data')
def get_data():
    data = {
        "message": "Ciao, questo è un messaggio API!",
    }
    return jsonify(data)

@app.route('/')
def index():
    return render_template('index.html', title="Movie List", films=lista)

app.run(debug=True)