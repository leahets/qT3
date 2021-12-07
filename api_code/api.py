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
        self.form = ""
        self.prefix_count = 0
        self.suffix_count = 0
        self.possible_prefixes = list()
        self.suffix = None
        self.future = False
        self.weak = False
        self.invalid = False
        self.dropped_prefixes = set()
        self.dropped_suffix = set()
        self.hollow = False
        self.defective = False
        self.geminated = True

    def __eq__(self, o) -> bool:
        if self.raw_text == o.raw_text:
            return True
        else:
            return False

    def __hash__(self) -> int:
        return hash(self.raw_text)


class Features:
    def __init__(self, tense, person, gender, number, mood):
        self.tense = tense
        self.number = number
        self.gender = gender
        self.person = person
        self.mood = mood
        self.prefix_count = 0
        self.suffix_count = 0
        self.hash_string = self.calc_hash_string()

    def __eq__(self, o) -> bool:
        return self.tense == o.tense and self.number == o.number and self.gender == o.gender and self.person == o.person and self.mood == o.mood

    def __hash__(self) -> int:
        return hash(self.hash_string)

    def calc_hash_string(self):
        """
        pretty much an 'encode features' method
        """
        hash_string = ""
        if self.tense == "past":
            hash_string += "p"
        elif self.tense == "present":
            hash_string += "r"

        hash_string += str(self.number)

        hash_string += self.gender[0]

        hash_string += str(self.person)

        hash_string += self.mood[0]

        return hash_string


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

    # word = verb_base_algorithm.make_word(verb)
    words = verb_base_algorithm.full_pipeline(verb)


    # deconjugated_word_obj = verb_base_algorithm.deconjugate(word)

    # new_word = verb_base_algorithm.strip_fixes(deconjugated_word_obj)
    # form, new_word = verb_base_algorithm.which_form(new_word)
    all_words = []
    for word in words:
        features_list = []
        for feature in word.features:
            new_feature_format = {"tense": feature.tense, "number": feature.number, "gender":feature.gender, "person":feature.person, "mood":feature.mood}
            features_list.append(new_feature_format)

        dict_word = {"word": verb, "form": word.form, "features": features_list, "root": word.root}
        all_words.append(json.dumps(dict_word))
    return json.dumps(all_words)#json.dumps(dict_word)
