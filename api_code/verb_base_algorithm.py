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

    if base_verb[0] == "أ" and 4 not in verb.checked_forms:
        print("checking form iv")
        if(check_iv(verb)):
            return "Form IV", verb
    else:
        if base_verb[0] == "ا":
            if base_verb[1] == "ن" and 7 not in verb.checked_forms:
                print("checking form vii")
                if(check_vii(verb)):
                    return "Form VII", verb
            else:
                if base_verb[1] == "س" and 10 not in verb.checked_forms:
                    print("checking form x")
                    if(check_x(verb)):
                        return "Form X", verb
                else:
                    if base_verb[2] == "ت" and 8 not in verb.checked_forms:
                        print("checking form viii")
                        if(check_viii(verb)):
                            return "Form VIII", verb
        else:
            if base_verb[0] == "ت":
                if base_verb[2] == "ا" and 6 not in verb.checked_forms:
                    print("checking form vi")
                    if(check_vi(verb)):
                        return "Form VI", verb
                if base_verb[3] == "ّ" and 5 not in verb.checked_forms:
                    print("checking form v")
                    if(check_v(verb)):
                        return "Form V", verb
            else:
                # 1st letter is in root
                if base_verb[1] == "ا" and 3 not in verb.checked_forms:
                    print("checking form iii")
                    if(check_iii(verb)):
                        return "Form III", verb
                else:
                    if base_verb[2] == "ّ" and 2 not in verb.checked_forms:
                        print("checking form ii")
                        if(check_ii(verb)):
                            return "Form II", verb
                    else:
                        if len(base_verb) == 3 and 1 not in verb.checked_forms:
                            print("checking form i")
                            if(check_i(verb)):
                                return "Form I", verb
                        else:
                            print("no form found")
                            return "Not a verb"


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
                if len(word.third_past) == 6:
                    root = root + base_verb[3]
                    root = root + base_verb[4]
                    root = root + base_verb[5]
                    word.root = root
                    return True
                else:
                    return False
                    ##LOOP HERE
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
    person_code = int(code[1])
    gender_code = code[2]
    number_code = int(code[3])
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


def create_features():
    global p3m1n
    p3m1n = decode_features('p3m1n')
    global p1n1n
    p1n1n = decode_features('p1n1n')
    global p2m1n
    p2m1n = decode_features('p2m1n')
    global p2f1n
    p2f1n = decode_features('p2f1n')
    global p3f1n
    p3f1n = decode_features('p3f1n')
    global p3f3n
    p3f3n = decode_features('p3f3n')
    global p3m2n
    p3m2n = decode_features('p3m2n')
    global p1n3n
    p1n3n = decode_features('p1n3n')
    global p3m3n
    p3m3n = decode_features('p3m3n')
    global p3f2n
    p3f2n = decode_features('p3f2n')
    global p2m2n
    p2m2n = decode_features('p2m2n')
    global p2f2n
    p2f2n = decode_features('p2f2n')
    global p2m3n
    p2m3n = decode_features('p2m3n')
    global p2f3n
    p2m3n = decode_features('p2f3n')
    global r1n1i
    r1n1i = decode_features('r1n1i')
    global r1n1s
    r1n1s = decode_features('r1n1s')
    global r1n1j
    r1n1j = decode_features('r1n1j')
    global r1n3i
    r1n3i = decode_features('r1n3i')
    global r1n3s
    r1n3s = decode_features('r1n3s')
    global r1n3j
    r1n3j = decode_features('r1n3j')
    global r2m1i
    r2m1i = decode_features('r2m1i')
    global r2m1s
    r2m1s = decode_features('r2m1s')
    global r2m1j
    r2m1j = decode_features('r2m1j')
    global r3f1i
    r3f1i = decode_features('r3f1i')
    global r3f1s
    r3f1s = decode_features('r3f1s')
    global r3f1j
    r3f1j = decode_features('r3f1j')
    global r2f3i
    r2f3i = decode_features('r2f3i')
    global r2f3s
    r2f3s = decode_features('r2f3s')
    global r2f3j
    r2f3j = decode_features('r2f3j')
    global r2m2i
    r2m2i = decode_features('r2m2i')
    global r2f2i
    r2f2i = decode_features('r2f2i')
    global r3f2i
    r3f2i = decode_features('r3f2i')
    global r2m3i
    r2m3i = decode_features('r2m3i')
    global r2f1i
    r2f1i = decode_features('r2f1i')
    global r2m2s
    r2m2s = decode_features('r2m2s')
    global r2m2j
    r2m2j = decode_features('r2m2j')
    global r2f2s
    r2f2s = decode_features('r2f2s')
    global r2f2j
    r2f2j = decode_features('r2f2j')
    global r3f2s
    r3f2s = decode_features('r3f2s')
    global r3f2j
    r3f2j = decode_features('r3f2j')
    global r2m3s
    r2m3s = decode_features('r2m3s')
    global r2m3j
    r2m3j = decode_features('r2m3j')
    global r2f1s
    r2f1s = decode_features('r2f1s')
    global r2f1j
    r2f1j = decode_features('r2f1j')
    global r3m1i
    r3m1i = decode_features('r3m1i')
    global r3m1s
    r3m1s = decode_features('r3m1s')
    global r3m1j
    r3m1j = decode_features('r3m1j')
    global r3f3i
    r3f3i = decode_features('r3f3i')
    global r3f3s
    r3f3s = decode_features('r3f3s')
    global r3f3j
    r3f3j = decode_features('r3f3j')
    global r3m2i
    r3m2i = decode_features('r3m2i')
    global r3m3i
    r3m3i = decode_features('r3m3i')
    global r3m2s
    r3m2s = decode_features('r3m2s')
    global r3m2j
    r3m2j = decode_features('r3m2j')
    global r3m3s
    r3m3s = decode_features('r3m3s')
    global r3m3j
    r3m3j = decode_features('r3m3j')


def deconjugate(word):
    verb = word.conjugated
    first_letter = verb[0]
    last_letter = verb[-1]
    second_last = verb[-2]
    third_last = verb[-3]
    if first_letter not in ("أ", "ن", "ت", "ي"):
        # Prefix 1 (None)
        if last_letter not in ("ت", "ن", "ا", "ي", "م", "ّ"):
            # Suffix 1 (None)
            word.features.add(p3m1n)
        elif last_letter == "ت":
            # Suffix 2 (ta)
            word.suffix_count += 1
            word.features.add(p1n1n)
            word.features.add(p2m1n)
            word.features.add(p2f1n)
            word.features.add(p3f1n)
        elif last_letter == "ن":
            # Suffix 3 (nun)
            word.suffix_count += 1
            word.features.add(p3f3n)
        elif last_letter == "ا":
            # Suffix 4 (alif)
            # AMBIGUOUS CASE, need to figure out how to check for p3m2n in multiple verb forms
            word.suffix_count += 1
            word.features.add(p3m2n)
            if second_last == "ن":
                # Suffix 4-1 (نا)
                word.suffix_count += 1
                word.features.add(p1n3n)
            elif second_last == "و":
                # Suffix 4-2 (وا)
                word.suffix_count += 1
                word.features.add(p3m3n)
            elif second_last == "ت":
                # suffix 4-3 (تا)
                word.suffix_count += 1
                word.features.add(p3f2n)
            elif second_last == "م":
                # Suffix 4-4 (تما)
                if third_last == "ت":
                    word.suffix_count += 2
                    word.features.add(p2m2n)
                    word.features.add(p2f2n)
                else:
                    print("UNCERTAIN")
    elif first_letter == "أ":
        # Prefix 2 (أ)
        word.prefix_count += 1
        if last_letter not in ("ت", "ن", "ا", "ي", "م", "ّ"):
            # Suffix 1 (None)
            word.features.add(r1n1i)
            word.features.add(r1n1s)
            word.features.add(r1n1j)
        else:
            print(
                "THIS IS PROBABLY FORM IV - but actually uncertain because why are we checking the suffix")
    elif first_letter == "ن":
        # Prefix 3 (ن)
        word.prefix_count += 1
        if last_letter not in ("ت", "ن", "ا", "ي", "م", "ّ"):
            # Suffix 1 (None)
            word.features.add(r1n3i)
            word.features.add(r1n3s)
            word.features.add(r1n3j)
        else:
            print("could still be first person plural present")
    elif first_letter == "ت":
        # Prefix 4 (ta)
        word.prefix_count += 1
        if last_letter not in ("ت", "ن", "ا", "ي", "م", "ّ"):
            # Suffix 1 (None)
            word.features.add(r2m1i)
            word.features.add(r2m1s)
            word.features.add(r2m1j)
            word.features.add(r3f1i)
            word.features.add(r3f1s)
            word.features.add(r3f1j)
        elif last_letter == "ن":
            word.suffix_count += 1
            if second_last not in ("ا", "و", "ي"):
                # Suffix 3 (nun)
                word.features.add(r2f3i)
                word.features.add(r2f3s)
                word.features.add(r2f3j)
            elif second_last == "ا":
                # Suffix 3-1 (ان)
                word.suffix_count += 1
                word.features.add(r2m2i)
                word.features.add(r2f2i)
                word.features.add(r3f2i)
            elif second_last == "و":
                # Suffix 3-2 (ون)
                word.suffix_count += 1
                word.features.add(r2m3i)
            elif second_last == "ي":
                # Suffix 3-3 (ين)
                word.suffix_count += 1
                word.features.add(r2f1i)
        elif last_letter == "ا":
            word.suffix_count += 1
            if second_last not in ("ن", "و"):
                # Suffix 4 (ا)
                word.features.add(r2m2s)
                word.features.add(r2m2j)
                word.features.add(r2f2s)
                word.features.add(r2f2j)
                word.features.add(r3f2s)
                word.features.add(r3f2j)
            elif second_last == "و":
                # Suffix 4-2 (وا)
                word.suffix_count += 1
                word.features.add(r2m3s)
                word.features.add(r2m3j)
        elif last_letter == "ي":
            # Suffix 5 (ي)
            word.suffix_count += 1
            word.features.add(r2f1s)
            word.features.add(r2f1j)
    elif first_letter == "ي":
        # Prefix 5 (yaa)
        word.prefix_count += 1
        if last_letter not in ("ت", "ن", "ا", "ي", "م", "ّ"):
            # Suffix 1 (None)
            word.features.add(r3m1i)
            word.features.add(r3m1s)
            word.features.add(r3m1j)
        elif last_letter == "ن":
            word.suffix_count += 1
            if second_last not in ("ا", "و"):
                # Suffix 3 (nun)
                word.features.add(r3f3i)
                word.features.add(r3f3s)
                word.features.add(r3f3j)
            elif second_last == "ا":
                # Suffix 3-1 (ان)
                word.suffix_count += 1
                word.features.add(r3m2i)
            elif second_last == "و":
                # Suffix 3-2 (ون)
                word.suffix_count += 1
                word.features.add(r3m3i)
        elif last_letter == "ا":
            word.suffix_count += 1
            if second_last not in ("ن", "و"):
                # Suffix 4 (alif)
                word.suffix_count += 1
                word.features.add(r3m2s)
                word.features.add(r3m2j)
            elif second_last == "و":
                # Suffix 4-2 (وا)
                word.suffix_count += 1
                word.features.add(r3m3s)
                word.features.add(r3m3j)
    return word

def strip_fixes(word):
    print('\n')
    print(word.raw_text)
    no_prefix = word.raw_text[word.prefix_count:]
    no_suffix = no_prefix[0:len(no_prefix) - word.suffix_count]
    word.third_past = no_suffix
    return word


def print_word(word):
    print("Raw text: " + word.raw_text)
    print("Conjugated form: " + word.conjugated)
    print("Base form: " + word.third_past)

    feature_counter = 1
    for item in word.features:
        print("FEATURE SET " + str(feature_counter))
        print_features(item)
        feature_counter += 1

    print("This verb has been checked for the following forms: ")
    print(word.checked_forms)
    print("The root of this word is " + word.root)


def print_features(f):
    print("This word is in the " + f.tense + " tense.")
    print("This word is in the " + str(f.person) + " person.")
    print("This word is " + f.gender)
    print("This word refers to " + str(f.number) + " people.")
    print("This word is in the " + f.mood + " mood.")


create_features()
test_word = Word("يكتبون")
deconjugate(test_word)


strip_fixes(test_word)
which_form(test_word)
print_word(test_word)
