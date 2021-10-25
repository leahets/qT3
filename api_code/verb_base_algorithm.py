# test verbs should be in 3rd person past tense singular (rightmost column of form chart)

output_file_name = "output.txt"

i = 0


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


class Features:
    def __init__(self, tense, person, gender, number, mood):
        self.tense = tense
        self.number = number
        self.gender = gender
        self.person = person
        self.mood = mood


def file_writer(text, file_name):
    global i
    i = i + 1
    f = open(file_name, "a")
    f.write('\n' + str(i) + '\n')
    f.write(text)
    f.close()


def make_word(verb):
    return Word(verb)


def which_form(verb):
    base_verb = verb.third_past

    if base_verb[0] == "أ":
        print("checking form iv")
        if(check_iv(verb)):
            return "Form IV"
    else:
        if base_verb[0] == "ا":
            if base_verb[1] == "ن":
                print("checking form vii")
                if(check_vii(verb)):
                    return "Form VII"
            else:
                if base_verb[1] == "س":
                    print("checking form x")
                    if(check_x(verb)):
                        return "Form X"
                else:
                    if base_verb[2] == "ت":
                        print("checking form viii")
                        if(check_viii(verb)):
                            return "Form VIII"
        else:
            if base_verb[0] == "ت":
                if base_verb[2] == "ا":
                    print("checking form vi")
                    if(check_vi(verb)):
                        return "Form VI"
                if base_verb[3] == "ّ":
                    print("checking form v")
                    if(check_v(verb)):
                        return "Form V"
            else:
                # 1st letter is in root
                if base_verb[1] == "ا":
                    print("checking form iii")
                    if(check_iii(verb)):
                        return "Form III"
                else:
                    if base_verb[2] == "ّ":
                        print("checking form ii")
                        if(check_ii(verb)):
                            return "Form II"
                    else:
                        if len(base_verb) == 3:
                            print("checking form i")
                            if(check_i(verb)):
                                return "Form I"
                        else:
                            print("no form found")


def check_i(word):
    word.checked_forms.add(1)
    base_verb = word.third_past
    root = ""
    if len(base_verb) == 3:
        root = root + base_verb[0]
        root = root + base_verb[1]
        root = root + base_verb[2]
        word.root = root
        return True
    else:
        return False


def check_ii(word):
    word.checked_forms.add(2)
    base_verb = word.third_past
    root = ""
    root = root + base_verb[0]
    root = root + base_verb[1]
    if base_verb[2] == "ّ":
        root = root + base_verb[3]
        word.root = root
        return True
    else:
        return False


def check_iii(word):
    word.checked_forms.add(3)
    base_verb = word.third_past
    root = ""
    root = root + base_verb[0]
    if base_verb[1] == "ا":
        root = root + base_verb[2]
        root = root + base_verb[3]
        word.root = root
        return True
    else:
        return False


def check_iv(word):
    word.checked_forms.add(4)
    base_verb = word.third_past
    root = ""
    if base_verb[0] == "أ":
        root = root + base_verb[1]
        root = root + base_verb[2]
        root = root + base_verb[3]
        word.root = root
        return True
    else:
        return False


def check_v(word):
    word.checked_forms.add(5)
    base_verb = word.third_past
    root = ""
    if base_verb[0] == "ت":
        root = root + base_verb[1]
        root = root + base_verb[2]
        if base_verb[3] == "ّ":
            root = root + base_verb[4]
            word.root = root
            return True
        else:
            return False
    else:
        return False


def check_vi(word):
    word.checked_forms.add(6)
    base_verb = word.third_past
    root = ""
    if base_verb[0] == "ت":
        root = root + base_verb[1]
        if base_verb[2] == "ا":
            root = root + base_verb[3]
            root = root + base_verb[4]
            word.root = root
            return True
        else:
            return False
    else:
        return False


def check_vii(word):
    word.checked_forms.add(7)
    base_verb = word.third_past
    root = ""
    if base_verb[0] == "ا":
        if base_verb[1] == "ن":
            root = root + base_verb[2]
            root = root + base_verb[3]
            root = root + base_verb[4]
            word.root = root
            return True
        else:
            return False
    else:
        return False


def check_viii(word):
    word.checked_forms.add(8)
    base_verb = word.third_past
    root = ""
    if base_verb[0] == "ا":
        root = root + base_verb[1]
        if base_verb[2] == "ت":
            root = root + base_verb[3]
            root = root + base_verb[4]
            word.root = root
            return True
        else:
            return False
    else:
        return False


def check_x(word):
    word.checked_forms.add(10)
    base_verb = word.third_past
    root = ""
    if base_verb[0] == "ا":
        if base_verb[1] == "س":
            if base_verb[2] == "ت":
                root = root + base_verb[3]
                root = root + base_verb[4]
                root = root + base_verb[5]
                word.root = root
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def check_form(base_verb, form):
    if form == 1:
        return check_i(base_verb)
    if form == 2:
        return check_ii(base_verb)
    if form == 3:
        return check_iii(base_verb)
    if form == 4:
        return check_iv(base_verb)
    if form == 5:
        return check_v(base_verb)
    if form == 6:
        return check_vi(base_verb)
    if form == 7:
        return check_vii(base_verb)
    if form == 8:
        return check_viii(base_verb)
    if form == 10:
        return check_x(base_verb)
    else:
        print("INVALID FORM")


def decode_features(code):
    tense = ""
    person = 0
    gender = ""
    number = 0
    mood = ""

    tense_code = code[0]
    person_code = code[1]
    gender_code = code[2]
    number_code = code[3]
    mood_code = code[4]

    if tense_code == 'p':
        tense = 'past'
    elif tense_code == 'r':
        tense = 'present'
    elif tense_code == 'f':
        tense = 'future'

    person = person_code

    if gender_code == 'm':
        gender = 'masculine'
    elif gender_code == 'f':
        gender = 'feminine'
    elif gender_code == 'n':
        gender = 'neutral'

    number = number_code

    if mood_code == 'i':
        mood = 'indicative'
    elif mood_code == 's':
        mood = 'subjunctive'
    elif mood_code == 'j':
        mood = 'jussive'
    elif mood_code == 'n':
        mood = 'none'

    return Features(tense, person, gender, number, mood)


def deconjugate(word):
    verb = word.conjugated
    first_letter = verb[0]
    last_letter = verb[-1]
    if first_letter not in ("أ", "ن", "ت", "ي"):
        # Prefix 1 (None)
        if last_letter not in ("ت", "ن", "ا", "ي", "م", "ّ"):
            # Suffix 1 (None)
            print("Third person singular masculine past")
            # word.features.add(p1m1n)
            word.third_past = verb
            word.person = 3
            word.plurality = 1
            word.gender = 'm'
            print_word(word)


def print_word(word):
    print("Raw text: " + word.raw_text)
    print("Conjugated form: " + word.conjugated)
    print("Base form: " + word.third_past)

    for item in word.features:
        print_features(item)

    print("This verb has been checked for the following forms: ")
    print(word.checked_forms)
    print("The root of this word is " + word.root)


def print_features(f):
    if f.person == 0:
        print("The person of this word is not known.")
    elif f.person == 1:
        print("This word is in the first person.")
    elif f.person == 2:
        print("This word is in the second person.")
    elif f.person == 3:
        print("This word is in the 3rd person.")

    if f.number == 0:
        print("The plurality of this word is not known.")
    elif f.number == 1:
        print("This word is singular.")
    elif f.number == 2:
        print("This word is dual.")
    elif f.number == 3:
        print("This word is plural.")

    if f.gender == 0:
        print("The gender of this word is unknown.")
    elif f.gender == 'm':
        print("This word is masculine.")
    elif f.gender == 'f':
        print("This word is feminine.")


# define_features()
test_word = Word("فعل")
deconjugate(test_word)
