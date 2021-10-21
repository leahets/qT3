import flask
from flask import request

app = flask.Flask(__name__)
#app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Testing 123</h1><p>This site is a prototype API. More soon</p>"

@app.route('/api/arabic/all', methods=['GET'])
def api_arabic():
    return "فعل"

@app.route('/api/arabic', methods=['GET'])
def api_word_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = request.args['id']
    else:
        return "Error: No id field provided. Please specify an id."

    # if id == 1:
    #     return "كتب"
    # if id == 2:
    #     return "مفعل"
    # if id == 3:
    #     return "تملك"
    if id == "مشمش":
        return id
    return "uh-oh"
