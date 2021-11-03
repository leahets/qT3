import flask
from flask import request
import verb_base_algorithm
import json


class Word:
    def __init__(self, raw_text):
        self.raw_text = raw_text
        self.conjugated = raw_text
        self.features = set()
        self.third_past = raw_text
        self.checked_forms = set()
        self.root = ""
        self.pos = "V"  # automatically verbs for now
        self.form = 0
        self.prefix_count = 0
        self.suffix_count = 0


class Features:
    def __init__(self, tense, person, gender, number, mood):
        self.tense = tense
        self.number = number
        self.gender = gender
        self.person = person
        self.mood = mood
        self.prefix_count = 0
        self.suffix_count = 0

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


@app.route('/api/verb', methods=['GET'])
def api_verb_info():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        verb = request.args['id']
    else:
        return "Error: No verb field provided. Please specify a verb."

    word = verb_base_algorithm.make_word(verb)

    deconjugated_word_obj = verb_base_algorithm.deconjugate(word)

    new_word = verb_base_algorithm.strip_fixes(deconjugated_word_obj)
    form, new_word = verb_base_algorithm.which_form(new_word)
    features_list = []
    for feature in deconjugated_word_obj.features:
        new_feature_format = {"tense": feature.tense, "number": feature.number, "gender":feature.gender, "person":feature.person, "mood":feature.mood}
        features_list.append(new_feature_format)

    dict_word = {"word": verb, "form": form, "features": features_list, "root": new_word.root}
    return json.dumps(dict_word)
