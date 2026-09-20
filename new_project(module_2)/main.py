from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')+render_template('index_1.html')

app.run(debug=True)