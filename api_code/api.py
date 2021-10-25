import flask
from flask import request
import verb_base_algorithm
import json


app = flask.Flask(__name__)
#app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Testing 123</h1><p>This site is a prototype API. More soon</p>"

@app.route('/api/arabic/all', methods=['GET'])
def api_arabic():
    return "فعل"

@app.route('/api/form', methods=['GET'])
def api_verb_form():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        verb = request.args['id']
    else:
        return "Error: No verb field provided. Please specify a verb."

    word = verb_base_algorithm.make_word(verb)
    form = verb_base_algorithm.which_form(word)
    dict_word = {"word": verb, "form": form}
    return json.dumps(dict_word)
