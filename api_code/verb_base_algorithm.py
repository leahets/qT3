# test verbs should be in 3rd person past tense singular (rightmost column of form chart)

output_file_name = "output.txt"
noun_prefixes = (("ب", "with, in, by"), ("ك", "same as"), ("و", "and"),
                 ("ال", "the"), ("ف", "then"), ("ل", "to, because"))

i = 0

verb_prefixes = (("س", "will", 2), ("و", "and", 0),
                 ("ف", "then", 0), ("ل", "to, because", 1))

verb_suffixes = (("ني", "me"), ("ك", "you"), ("ه", "him"), ("ها", "her"), ("كما", "you (dual)"), ("هما", "them (dual)"), ("نا", "us"),
                 ("كم", "you (plural masculine)"), ("كن", "you (plural feminine)"), ("هم", "them (plural masculine"), ("هن", "them (plural feminine)"))


class Word:
    def __init__(self, raw_text):
        self.raw_text = raw_text
        self.conjugated = raw_text
        self.features = set()
        self.third_past = raw_text
        self.checked_forms = set()
        self.root = ""
        self.form = ""
        self.prefix_count = 0  # for conjugations
        self.suffix_count = 0  # for conjugations
        self.possible_prefixes = list()
        #self.suffix = None
        self.future = False
        self.weak = False
        self.invalid = False
        self.dropped_prefixes = []
        self.dropped_suffix = set()
        self.hollow = False
        self.defective = False
        self.geminated = False
        self.assimilated = False

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


def file_writer(text, file_name):
    global i
    i = i + 1
    f = open(file_name, "a")
    f.write('\n' + str(i) + '\n')
    f.write(text)
    f.close()


def make_word(verb):
    return Word(verb)


def english_checker(text):
    for letter in text:
        if letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
            return True
    return False


def letter_assignment(text):
    word_length = len(text)
    if word_length >= 1:
        first_letter = text[0]
    else:
        first_letter = ' '

    if word_length >= 2:
        second_letter = text[1]
    else:
        second_letter = ' '

    if word_length >= 3:
        third_letter = text[2]
    else:
        third_letter = ' '

    if word_length >= 4:
        fourth_letter = text[3]
    else:
        fourth_letter = ' '

    if word_length >= 2:
        last_letter = text[-1]
    else:
        last_letter = ' '
    return first_letter, second_letter, third_letter, fourth_letter, last_letter


def which_form(verb):
    base_verb = verb.third_past
    length = len(base_verb)
    first_letter, second_letter, third_letter, fourth_letter, last_letter = letter_assignment(
        base_verb)

    if first_letter == "أ" and length == 4 and 4 not in verb.checked_forms:
        print("checking form iv")
        if(check_iv(verb)):
            return verb
    else:
        if first_letter == "ا":
            if second_letter == "ن" and length == 5 and 7 not in verb.checked_forms:
                print("checking form vii")
                if(check_vii(verb)):
                    return verb
            else:
                if second_letter == "س" and length == 6 and 10 not in verb.checked_forms:
                    print("checking form x")
                    if(check_x(verb)):
                        return verb
                else:
                    if third_letter == "ت" and length == 5 and 8 not in verb.checked_forms:
                        print("checking form viii")
                        if(check_viii(verb)):
                            return verb
        else:
            if first_letter == "ت":
                if third_letter == "ا" and length == 5 and 6 not in verb.checked_forms:
                    print("checking form vi")
                    if(check_vi(verb)):
                        return verb
                if fourth_letter == "ّ" and length == 5 and 5 not in verb.checked_forms:
                    print("checking form v")
                    if(check_v(verb)):
                        return verb
            else:
                # 1st letter is in root
                if second_letter == "ا" and length == 4 and 3 not in verb.checked_forms:
                    print("checking form iii")
                    if(check_iii(verb)):
                        return verb
                else:
                    if third_letter == "ّ" and length == 4 and 2 not in verb.checked_forms:
                        print("checking form ii")
                        if(check_ii(verb)):
                            return verb
                    else:
                        if length == 3 and 1 not in verb.checked_forms:
                            print("checking form i")
                            if(check_i(verb)):
                                return verb
                        else:
                            if (check_x(verb)):
                                return verb
                            elif (check_viii(verb)):
                                return verb
                            elif (check_viii_spelling(verb)):
                                return verb
                            else:
                                print("no form found")
                                print("checking 8 spelling rule")
                                if (check_viii_spelling(verb)):
                                    return verb
                                else:
                                    if verb.weak:
                                        verb.form = "Form I"
                                        return verb
                                    else:
                                        print(
                                            verb.raw_text + " is invalid because a form could not be found.")
                                        verb.invalid = True
                                        return verb


def check_i(word):
    word.checked_forms.add(1)
    word.checked_forms.add(14)
    base_verb = word.third_past
    first_letter, second_letter, third_letter, fourth_letter, last_letter = letter_assignment(
        base_verb)

    root = ""
    if len(base_verb) == 3:
        root = root + first_letter + ' '
        root = root + second_letter + ' '
        root = root + third_letter
        word.root = root
        # checking for form 14
        arbitrary_feature = word.features.pop()
        word.features.add(arbitrary_feature)
        tense = arbitrary_feature.tense
        if tense == "present" or word.raw_text[0] == "أ":
            word.form = "Form I/Form IV"
        else:
            word.form = "Form I"
        return True
    else:
        return False


def check_ii(word):
    word.checked_forms.add(2)
    word.checked_forms.add(25)
    base_verb = word.third_past
    first_letter, second_letter, third_letter, fourth_letter, last_letter = letter_assignment(
        base_verb)

    root = ""
    root = root + first_letter + ' '
    root = root + second_letter + ' '
    if third_letter == "ّ":
        root = root + fourth_letter
        word.root = root
        if word.raw_text[0] == "ت":
            word.form = "Form II/Form V"
        else:
            word.form = "Form II"
        return True
    else:
        return False


def check_iii(word):
    word.checked_forms.add(3)
    base_verb = word.third_past
    first_letter, second_letter, third_letter, fourth_letter, last_letter = letter_assignment(
        base_verb)

    root = ""
    root = root + first_letter + ' '
    if second_letter == "ا":
        root = root + third_letter + ' '
        root = root + fourth_letter
        word.root = root
        word.form = "Form III"
        return True
    else:
        return False


def check_iv(word):
    word.checked_forms.add(4)
    base_verb = word.third_past
    first_letter, second_letter, third_letter, fourth_letter, last_letter = letter_assignment(
        base_verb)

    root = ""
    if first_letter == "أ":
        root = root + second_letter + ' '
        root = root + third_letter + ' '
        root = root + fourth_letter
        word.root = root
        word.form = "Form IV"
        return True
    else:
        return False


def check_v(word):
    word.checked_forms.add(5)
    base_verb = word.third_past
    first_letter, second_letter, third_letter, fourth_letter, last_letter = letter_assignment(
        base_verb)

    if len(base_verb) >= 5:
        fifth_letter = base_verb[4]
    else:
        fifth_letter = ' '

    root = ""
    if first_letter == "ت":
        root = root + second_letter + ' '
        root = root + third_letter + ' '
        if fourth_letter == "ّ":
            root = root + fifth_letter
            word.root = root
            word.form = "Form V"
            return True
        else:
            return False
    else:
        return False


def check_vi(word):
    word.checked_forms.add(6)
    base_verb = word.third_past
    first_letter, second_letter, third_letter, fourth_letter, last_letter = letter_assignment(
        base_verb)

    if len(base_verb) >= 5:
        fifth_letter = base_verb[4]
    else:
        fifth_letter = ' '

    root = ""
    if first_letter == "ت":
        root = root + second_letter + ' '
        if third_letter == "ا":
            root = root + fourth_letter + ' '
            root = root + fifth_letter
            word.root = root
            word.form = "Form VI"
            return True
        else:
            return False
    else:
        return False


def check_vii(word):
    word.checked_forms.add(7)
    base_verb = word.third_past
    first_letter, second_letter, third_letter, fourth_letter, last_letter = letter_assignment(
        base_verb)

    if len(base_verb) >= 5:
        fifth_letter = base_verb[4]
    else:
        fifth_letter = ' '

    root = ""
    if first_letter == "ا":
        if second_letter == "ن":
            root = root + third_letter + ' '
            root = root + fourth_letter + ' '
            root = root + fifth_letter
            word.root = root
            word.form = "Form VII"
            return True
        else:
            return False
    else:
        return False


def check_viii(word):
    word.checked_forms.add(8)
    base_verb = word.third_past
    first_letter, second_letter, third_letter, fourth_letter, last_letter = letter_assignment(
        base_verb)

    if len(base_verb) >= 5:
        fifth_letter = base_verb[4]
    else:
        fifth_letter = ' '

    root = ""
    if len(word.features) != 0:
        arbitrary_feature = word.features.pop()
        word.features.add(arbitrary_feature)
        tense = arbitrary_feature.tense
        if tense == "past":
            if first_letter == "ا" or first_letter == "إ":
                root = root + second_letter + ' '
                if third_letter == "ت":
                    root = root + fourth_letter + ' '
                    root = root + fifth_letter
                    word.root = root
                    word.form = "Form VIII"
                    return True
                else:
                    return False
            else:
                return False
        else:
            if len(word.third_past) == 4:
                root = root + first_letter + ' '
                if second_letter == "ت":
                    root = root + third_letter + ' '
                    root = root + fourth_letter
                    word.root = root
                    word.form = "Form VIII"
                    return True
                else:
                    return False
            else:
                return False
    else:
        return False


def check_x(word):
    word.checked_forms.add(10)
    base_verb = word.third_past
    first_letter, second_letter, third_letter, fourth_letter, last_letter = letter_assignment(
        base_verb)

    if len(base_verb) >= 5:
        fifth_letter = base_verb[4]
    else:
        fifth_letter = ' '

    if len(base_verb) >= 6:
        sixth_letter = base_verb[5]
    else:
        sixth_letter = ' '

    root = ""
    if len(word.features) != 0:
        arbitrary_feature = word.features.pop()
        word.features.add(arbitrary_feature)
        tense = arbitrary_feature.tense
        if tense == "past":
            if first_letter == "ا":
                if second_letter == "س":
                    if third_letter == "ت":
                        if len(word.third_past) == 6:
                            root = root + fourth_letter + ' '
                            root = root + fifth_letter + ' '
                            root = root + sixth_letter
                            word.root = root
                            word.form = "Form X"
                            return True
                        else:
                            return False
                            # LOOP HERE
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            if first_letter == "س":
                if second_letter == "ت":
                    if len(word.third_past) == 5:
                        root = root + third_letter + ' '
                        root = root + fourth_letter + ' '
                        root = root + fifth_letter + ' '
                        word.root = root
                        word.form = "Form X"
                        return True
                    else:
                        return False
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
        base_verb.invalid = True
        print(base_verb.raw_text + " is invalid because a form could not be found.")


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


def end_geminated_check(word):
    if len(word.conjugated) >= 2:
        last_letter = word.conjugated[-1]
        second_last = word.conjugated[-2]
        if last_letter == "ّ" and second_last != "ن":
            word.geminated = True
            new_conjugated = word.conjugated[:-1]
            doubled_letter = second_last
            new_conjugated = new_conjugated + doubled_letter
            word.conjugated = new_conjugated
    return word


def deconjugate(word):
    word = end_geminated_check(word)
    verb = word.conjugated
    word_length = len(verb)
    if word_length >= 1:
        first_letter = verb[0]
    else:
        first_letter = None

    if word_length >= 2:
        last_letter = verb[-1]
    else:
        last_letter = None

    if word_length >= 3:
        second_last = verb[-2]
    else:
        second_last = None

    if word_length >= 4:
        third_last = verb[-3]
    else:
        third_last = None

    if first_letter not in ("أ", "ن", "ت", "ي"):
        # Prefix 1 (None)
        if last_letter not in ("ت", "ن", "ا"):
            # removed shadda, mim, yaa
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
    elif first_letter == "أ":
        # Prefix 2 (أ)
        word.prefix_count += 1
        if last_letter not in ("ن", "ا", "ي"):
            # removed taa, mim, shadda
            # Suffix 1 (None)
            word.features.add(r1n1i)
            word.features.add(r1n1s)
            word.features.add(r1n1j)
    elif first_letter == "ن":
        # Prefix 3 (ن)
        if word_length == 3:
            word.features.add(p3m1n)
        else:
            word.prefix_count += 1
            if last_letter not in ("ن", "ا", "ي"):
                # removed taa, mim, shadda
                # Suffix 1 (None)
                word.features.add(r1n3i)
                word.features.add(r1n3s)
                word.features.add(r1n3j)
    elif first_letter == "ت":
        # Prefix 4 (ta)
        word.prefix_count += 1
        if last_letter not in ("ن", "ا", "ي"):
            # removed taa, mim, shadda
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
            elif second_last == "ن":
                word.suffix_count += 1
                word.features.add(p1n3n)
        elif last_letter == "ي":
            # Suffix 5 (ي)
            word.suffix_count += 1
            word.features.add(r2f1s)
            word.features.add(r2f1j)
    elif first_letter == "ي":
        # Prefix 5 (yaa)
        word.prefix_count += 1
        if last_letter not in ("ن", "ا"):
            # *********THIS IS WHERE WE DELETED YAA
            # removed mim, taa, shadda
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
            elif second_last == "ن":
                word.suffix_count += 1
                word.features.add(p1n3n)
    return word


def strip_fixes(word):
    no_prefix = word.raw_text[word.prefix_count:]
    no_suffix = no_prefix[0:len(no_prefix) - word.suffix_count]
    word.third_past = no_suffix
    return word


def identify_prefixes(text):
    # create set of possible affixes if they overlap with list of ALL possible affixes
    # made using text, NOT word object, for looping function
    possible_prefixes = list()
    for prefix in verb_prefixes:
        if (text[0] == prefix[0]):
            possible_prefixes.append(prefix)
            text = text[1:]
            for prefix_2 in verb_prefixes:
                if(text[0] == prefix_2[0]):
                    possible_prefixes.append(prefix_2)
                    text = text[1:]
                    for prefix_3 in verb_prefixes:
                        if(text[0] == prefix_3[0]):
                            possible_prefixes.append(prefix_3)
                            text = text[1:]
    return possible_prefixes


def identify_suffix(text):
    # made using text, NOT word object, for looping function
    possible_suffix = None
    for suffix in verb_suffixes:
        suffix_length = len(suffix[0])
        if len(text) <= suffix_length:
            continue
        else:
            if suffix[0] == text[-suffix_length:]:
                possible_suffix = suffix
                break
    return possible_suffix


def print_word(word):
    print("Raw text: " + word.raw_text)
    print("Conjugated form: " + word.conjugated)
    print("Base form: " + word.third_past)
    print("Prefixes removed: " + str(word.dropped_prefixes))
    print("Suffix removed: " + str(word.dropped_suffix))

    feature_counter = 1
    for item in word.features:
        print("FEATURE SET " + str(feature_counter))
        print_features(item)
        feature_counter += 1

    print("This verb has been checked for the following forms: ")
    print(word.checked_forms)
    print("This verb is in form: " + str(word.form))
    print("The root of this word is " + word.root)
    print("This word may be weak:" + str(word.weak))
    print("This word is hollow: " + str(word.hollow))
    print("This word is defective: " + str(word.defective))
    print("This word is assimilated: " + str(word.assimilated))
    print("Invalid? " + str(word.invalid))


def print_features(f):
    print("This word is in the " + f.tense + " tense.")
    print("This word is in the " + str(f.person) + " person.")
    print("This word is " + f.gender)
    print("This word refers to " + str(f.number) + " people.")
    print("This word is in the " + f.mood + " mood.")


def check_double_hamza(word):
    if (word.raw_text[0]) == "آ":
        word.conjugated = "أ" + "أ" + word.raw_text[1:]
        word.raw_text = word.conjugated
    return word


def check_root_hamza(word):
    if word.root != "":
        for i in range(0, len(word.root)):
            if word.root[i] in ("أ", "ؤ", "ئ"):
                new_root = word.root[0:i] + "ء" + word.root[i+1:]
                word.root = new_root
                break
    return word


def check_invalid_preconjugate(word):
    if len(word.raw_text) <= 2:
        print(word.raw_text +
              " is invalid because there are only two letters before deconjugating.")
        word.invalid = True


def check_weak_postconjugate(word):
    if len(word.third_past) <= 2:
        word.weak = True
        if len(word.features) >= 1:
            feature = word.features.pop()
            word.features.add(feature)
            if feature.tense == "past":
                word.hollow = True
        ##here check feature set, if it's in xyz it's hollow else if it's in abc it's assimilated
        word.checked_forms.add(1)
        word.form = "Form I"


def check_prefix_order(word):
    if len(word.dropped_prefixes) > 0:
        print("prefixes dropped:")
        length = len(word.dropped_prefixes)
        if length >= 2:
            for i in range(0, length-1):
                pre = word.dropped_prefixes[i]
                next_pre = word.dropped_prefixes[i+1]
                if pre[2] >= next_pre[2]:
                    print(
                        word.raw_text + " is invalid because the prefixes are conflicting or out of order.")
                    word.invalid = True
    return word


def sanity_check(word):
    # If there is a shadda in the root, it's not correct
    shadda_in_root(word)
    # If verb is hollow and past tense with alif in middle, adjust features to match appropriate 1stp/2ndp vs 3rdp feminine
    check_hollow_past(word)
    # If verb is marked as future, features must be in present
    # If verb is marked as future and form is 14, form is actually I -> correct features to match
    check_future(word)
    # If verb has multiple prefixes, check that they're in proper order
    check_prefix_order(word)

    return word
    # If in form 14 or 25, word must also have features 14 and 25

    # Vowel dropping - check that features match with possibility of a hollow verb


def check_future(word):
    mark_future(word)
    for f in word.features:
        tense = f.tense
        if word.future == True and tense == 'past':
            print(word.raw_text +
                  " is invalid because it has the future prefix but is in the past tense.")
            word.invalid = True
            return word
        elif word.future == True and tense == 'present':
            if word.form == "Form I/Form IV":
                word.form = "Form I"
            if word.form == "Form II/Form V":
                word.form = "Form II"
            f.tense = "future"
    return word


def create_possible_words(text):
    text_possibilities = list()
    prefixes = identify_prefixes(text)
    print("PREFIXES:")
    print(prefixes)
    suffix = identify_suffix(text)
    print("SUFFIX:")
    print(suffix)
    total_prefixes = len(prefixes)
    print("NUMBER OF PREFIXES:")
    print(total_prefixes)

    dropped_prefixes = list()
    dropped_suffix = set()
    dropped_text = text
    # Drop everything
    if suffix != None:
        dropped_text = dropped_text[:-len(suffix[0])]
        dropped_suffix.add(suffix)
        # print(dropped_text)
    dropped_text = dropped_text[total_prefixes:]
    dropped_prefixes = list(prefixes)
    print("\nDropping all prefixes and suffixes:")
    # this is where we would check for 2 letters and put the pipeline
    # add all returned words to set, then sanity check every word in set after
    print(dropped_text)
    bald_word = Word(dropped_text)
    bald_word.dropped_prefixes = dropped_prefixes
    bald_word.dropped_suffix = dropped_suffix
    text_possibilities.append(bald_word)

    # Drop suffix, keep all prefixes
    dropped_text = text
    dropped_prefixes = list()
    dropped_suffix = set()
    if suffix != None:
        dropped_text = dropped_text[:-len(suffix[0])]
        dropped_suffix.add(suffix)
    print("\nDropping suffix, keeping prefix")
    print(dropped_text)
    bald_word = Word(dropped_text)
    bald_word.dropped_prefixes = dropped_prefixes
    bald_word.dropped_suffix = dropped_suffix
    text_possibilities.append(bald_word)

    # Drop suffix, remove prefixes one at a time (keeping order)
    dropped_text = text
    dropped_prefixes = list()
    dropped_suffix = set()
    if suffix != None:
        dropped_text = dropped_text[:-len(suffix[0])]
        dropped_suffix.add(suffix)
    i = 0
    while i <= total_prefixes:
        dropped_text = dropped_text[i:]
        print("\nDropping suffix, dropping prefixes gradually at step:")
        print(i)
        print(dropped_text)
        if i < total_prefixes:
            dropped_prefixes.append(prefixes[i])
        bald_word = Word(dropped_text)
        bald_word.dropped_prefixes = dropped_prefixes
        bald_word.dropped_suffix = dropped_suffix
        text_possibilities.append(bald_word)
        i += 1

    # Keep suffix, remove prefixes one at a time (keeping order)
    # Note: If there is no suffix, this step already happened in the previous step
    dropped_text = text
    dropped_prefixes = list()
    dropped_suffix = set()
    if suffix != None:
        j = 0
        print(total_prefixes)
        while j < total_prefixes:
            # changed from <= to < for out of bounds errors, hopefully this fixes it
            dropped_text = dropped_text[j:]
            dropped_prefixes.append(prefixes[j])
            print("\nKeeping suffix, dropping prefixes gradually at step:")
            print(j)
            print(dropped_text)
            bald_word = Word(dropped_text)
            bald_word.dropped_prefixes = dropped_prefixes
            bald_word.dropped_suffix = dropped_suffix
            text_possibilities.append(bald_word)
            j += 1

    # Keep suffix, drop all prefixes
    dropped_text = text
    dropped_prefixes = list()
    dropped_suffix = set()
    if suffix != None:
        dropped_text = dropped_text[total_prefixes:]
        print("\nKeeping suffix, dropping ALL prefixes")
        for prefix in prefixes:
            dropped_prefixes.append(prefix)
            print(dropped_text)
        bald_word = Word(dropped_text)
        bald_word.dropped_prefixes = dropped_prefixes
        bald_word.dropped_suffix = dropped_suffix
        text_possibilities.append(bald_word)

    # Keep everything
    dropped_text = text
    dropped_prefixes = list()
    dropped_suffix = set()
    print("\nKeeping everything")
    print(dropped_text)
    bald_word = Word(dropped_text)
    bald_word.dropped_prefixes = dropped_prefixes
    bald_word.dropped_suffix = dropped_suffix
    text_possibilities.append(bald_word)
    # order to check:
    # drop everything (first step of next step, technically)
    # (suffix dropped) add prefix left to right
    # add suffix, add prefix left to right
    # add everything (last step of previous step, technically)

    # order to check:
    # drop all prefixes and suffixes
    # from raw text, drop suffix, keep all prefixes
    # from raw text, drop suffix, drop prefixes right to left
    # from raw text, keep suffix, drop prefixes right to left
    # from raw text, keep suffix, keep prefixes
    # pipeline(text)
    return text_possibilities


def full_pipeline(text):
    if english_checker(text):
        bad_word = Word(text)
        bad_word.form = "English"
        bad_list = list()
        bad_list.append(bad_word)
        return bad_list
    else:
        create_features()
        full_text_possibilities = create_possible_words(text)
        for ex_word in full_text_possibilities:
            print(ex_word.raw_text)
        text_possibilities = list(dict.fromkeys(full_text_possibilities))
        # this^ removes duplicates
        final_words = list()

        for possible_word in text_possibilities:
            print("POSSIBLE WORD:")
            print_word(possible_word)
            word = pipeline(possible_word)
            word = sanity_check(word)
            if not word.invalid:
                final_words.append(word)

    if len(final_words) == 0:
        no_word = Word(text)
        no_word.form = "None"
        final_words.append(no_word)
    return final_words


def mark_future(word):
    # if sin is in set of prefixes, mark as future
    sin = ("س", "will")
    if sin in word.dropped_prefixes:
        word.future = True
    return word


def shadda_in_root(word):
    if "ّ" in word.root:
        print(word.raw_text + " is invalid because there is a shadda in the root.")
        word.invalid = True
    return word


def weak_in_root(word):
    weak_roots = ["و", "ا", "ي", "ى"]
    for letter in word.root:
        if letter in weak_roots:
            word.weak = True
    check_hollow_defective(word)
    return word


def check_hollow_defective(word):
    if word.weak:
        print(len(word.features))
        if len(word.features) >= 1:
            arbitrary_feature = word.features.pop()
            word.features.add(arbitrary_feature)
            tense = arbitrary_feature.tense
            print_features(arbitrary_feature)
            if tense == "past":
                hollow_letter = word.root[2]
                new_letter = " "
                if hollow_letter == "ا":
                    word.hollow = True
                    new_letter = "و/ي"
                    new_root = word.root[0:2] + new_letter + word.root[3:]
                    word.root = new_root
                else:
                    defective_letter = word.root[-1]
                    new_letter = " "
                    if defective_letter in ["ي", "و", "ى"]:
                        word.defective = True
                        if defective_letter == "ي":
                            new_letter = "ى"
                        elif defective_letter == "ى":
                            new_letter = "ي"
                        elif defective_letter == "و":
                            new_letter = "ا"
                        new_root = word.root[0:-1] + new_letter
                        word.root = new_root
                    else:
                        word.assimilated = True
    return word


def check_root_filled(word):
    if word.root == "":
        root_list = []
        if len(word.raw_text) == 3 and not word.weak:
            for letter in word.raw_text:
                root_list.append(letter)
            word.root = str.join(' ', root_list)
        else:
            for letter in word.third_past:
                root_list.append(letter)
            word.root = str.join(' ', root_list)
    return word


def check_viii_spelling(word):
    word.checked_forms.add(80)
    base_verb = word.third_past
    first_letter, second_letter, third_letter, fourth_letter, last_letter = letter_assignment(
        base_verb)
    if len(base_verb) >= 5:
        fifth_letter = base_verb[4]
    else:
        fifth_letter = ' '

    root = ""
    if len(word.features) != 0:
        arbitrary_feature = word.features.pop()
        word.features.add(arbitrary_feature)
        tense = arbitrary_feature.tense
        if tense == "past":
            if first_letter == "ا" or first_letter == "إ":
                # change below
                if third_letter == "ّ" and len(base_verb) == 5:
                    if second_letter == "ط" or "ظ":
                        root = root + second_letter + ' '
                        root = root + fourth_letter + ' '
                        root = root + fifth_letter
                        word.root = root
                        word.form = "Form VIII, spelling shift"
                        return True
                    elif second_letter == "ت":
                        # possibly taa, possibly assimilated
                        word.weak = True
                        root = root + second_letter + ' '
                        root = root + fourth_letter + ' '
                        root = root + fifth_letter
                        word.root = root
                        word.form = "Form VIII, spelling shift"
                        return True
                    elif second_letter == "د":
                        root = root + "د/ذ"
                        root = root + fourth_letter + ' '
                        root = root + fifth_letter
                        word.root = root
                        word.form = "Form VIII, spelling shift"
                        return True
                elif third_letter == "ط" and second_letter == "ص" or "ض":
                    root = root + second_letter + ' '
                    root = root + fourth_letter + ' '
                    root = root + fifth_letter
                    word.root = root
                    word.form = "Form VIII, spelling shift"
                    return True
                elif third_letter == "د" and second_letter == "ز":
                    root = root + second_letter + ' '
                    root = root + fourth_letter + ' '
                    root = root + fifth_letter
                    word.root = root
                    word.form = "Form VIII, spelling shift"
                    return True
                else:
                    return False
            else:
                return False
        else:
            if len(word.third_past) == 4:
                root = root + first_letter + ' '
                # change below
                if second_letter == "ّ":
                    if first_letter == "ط" or "ظ":
                        root = root + third_letter + ' '
                        root = root + fourth_letter
                        word.root = root
                        word.form = "Form VIII, spelling shift"
                        return True
                    elif first_letter == "ت":
                        # possibly taa, possibly assimilated
                        word.weak = True
                        root = root + third_letter + ' '
                        root = root + fourth_letter
                        word.root = root
                        word.form = "Form VIII, spelling shift"
                        return True
                    elif first_letter == "د":
                        root = "د/ذ "
                        root = root + third_letter + ' '
                        root = root + fourth_letter
                        word.root = root
                        word.form = "Form VIII, spelling shift"
                        return True
                elif second_letter == "ط" and first_letter == "ص" or "ض":
                    root = root + first_letter + ' '
                    root = root + third_letter + ' '
                    root = root + fourth_letter
                    word.root = root
                    word.form = "Form VIII, spelling shift"
                    return True
                elif second_letter == "د" and first_letter == "ز":
                    root = root + first_letter + ' '
                    root = root + third_letter + ' '
                    root = root + fourth_letter
                    word.root = root
                    word.form = "Form VIII, spelling shift"
                    return True
                else:
                    return False
            else:
                return False
    else:
        return False


def check_assimilated(word):
    if word.assimilated:
        if len(word.third_past) == 2:
            if word.suffix_count == 1:
                word.assimilated = True
                new_root = "و/ي " + word.root
                word.root = new_root
    return word


def check_hollow_past(word):
    if word.hollow:
        if word.conjugated[-1] == "ت":
            if p3f1n in word.features:
                if len(word.conjugated) == 4:
                    # feature set should only have past 3rd feminine singular
                    word.features.discard(p1n1n)
                    word.features.discard(p2f1n)
                    word.features.discard(p2m1n)
                elif len(word.conjugated) == 3:
                    word.features.discard(p3f1n)
                    # feature set should not have past 3rd feminine singular
                    # feature set should have past 1st person, 2nd person masculine singular, 2nd person feminine singular
    return word


def pipeline(test_word):
    check_invalid_preconjugate(test_word)
    check_double_hamza(test_word)
    deconjugate(test_word)
    strip_fixes(test_word)
    check_weak_postconjugate(test_word)
    which_form(test_word)
    check_root_filled(test_word)
    check_root_hamza(test_word)
    weak_in_root(test_word)
    # check_assimilated(test_word)
    return test_word


complete_possible_words = full_pipeline("صمت")

# nam in past tense being marked as present

for word in complete_possible_words:
    print('\n')
    print_word(word)
