from flask import Flask, render_template_string, request
import re

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    text = re.sub('_', ' ', text)
    return 'C {}'.format(text)

@app.route('/python/<text>', strict_slashes=False)
def python(text):
    text = re.sub('_', ' ', text)
    return 'Python {}'.format(text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
