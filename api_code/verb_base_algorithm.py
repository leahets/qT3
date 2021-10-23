# test verbs should be in 3rd person past tense singular (rightmost column of form chart)

output_file_name = "output.txt"

i = 0


class Word:
    def __init__(self, raw_text):
        self.raw_text = raw_text
        self.third_past = raw_text
        self.checked_forms = set()
        self.root = ""
        self.pos = "V"  # automatically verbs for now


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


test_word = Word("فعل")
which_form(test_word)
