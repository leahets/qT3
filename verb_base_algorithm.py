input_verb = "test test test"
# should be in 3rd person past tense singular (rightmost column of form chart)

output_file_name = "output.txt"

i = 0


def file_writer(text, file_name):
    global i
    i = i + 1
    f = open(file_name, "a")
    f.write('\n' + str(i) + '\n')
    f.write(text)
    f.close()


def which_form(base_verb):
    if base_verb[0] == "أ":
        print("checking form iv")
        print(check_iv(base_verb))
    else:
        if base_verb[0] == "ا":
            if base_verb[1] == "ن":
                print("checking form vii")
                print(check_vii(base_verb))
            else:
                if base_verb[1] == "س":
                    print("checking form x")
                    print(check_x(base_verb))
                else:
                    if base_verb[2] == "ت":
                        print("checking form viii")
                        print(check_viii(base_verb))
        else:
            if base_verb[0] == "ت":
                if base_verb[2] == "ا":
                    print("checking form vi")
                    print(check_vi(base_verb))
                if base_verb[3] == "ّ":
                    print("checking form v")
                    print(check_v(base_verb))
            else:
                # 1st letter is in root
                if base_verb[1] == "ا":
                    print("checking form iii")
                    print(check_iii(base_verb))
                else:
                    if base_verb[2] == "ّ":
                        print("checking form ii")
                        print(check_ii(base_verb))
                    else:
                        if len(base_verb) == 3:
                            print("checking form i")
                            print(check_i(base_verb))
                        else:
                            print("no form found")


def check_i(base_verb):
    root = ""
    if len(base_verb) == 3:
        root = root + base_verb[0]
        root = root + base_verb[1]
        root = root + base_verb[2]
        return True, root
    else:
        return False, ""


def check_ii(base_verb):
    root = ""
    root = root + base_verb[0]
    root = root + base_verb[1]
    if base_verb[2] == "ّ":
        root = root + base_verb[3]
        return True, root
    else:
        return False, ""


def check_iii(base_verb):
    root = ""
    root = root + base_verb[0]
    if base_verb[1] == "ا":
        root = root + base_verb[2]
        root = root + base_verb[3]
        return True, root
    else:
        return False, ""


def check_iv(base_verb):
    root = ""
    if base_verb[0] == "أ":
        root = root + base_verb[1]
        root = root + base_verb[2]
        root = root + base_verb[3]
        return True, root
    else:
        return False, ""


def check_v(base_verb):
    root = ""
    if base_verb[0] == "ت":
        root = root + base_verb[1]
        root = root + base_verb[2]
        if base_verb[3] == "ّ":
            root = root + base_verb[4]
            return True, root
        else:
            return False, ""
    else:
        return False, ""


def check_vi(base_verb):
    root = ""
    if base_verb[0] == "ت":
        root = root + base_verb[1]
        if base_verb[2] == "ا":
            root = root + base_verb[3]
            root = root + base_verb[4]
            return True, root
        else:
            return False, ""
    else:
        return False, ""


def check_vii(base_verb):
    root = ""
    if base_verb[0] == "ا":
        if base_verb[1] == "ن":
            root = root + base_verb[2]
            root = root + base_verb[3]
            root = root + base_verb[4]
            return True, root
        else:
            return False, ""
    else:
        return False, ""


def check_viii(base_verb):
    root = ""
    if base_verb[0] == "ا":
        root = root + base_verb[1]
        if base_verb[2] == "ت":
            root = root + base_verb[3]
            root = root + base_verb[4]
            return True, root
        else:
            return False, ""
    else:
        return False, ""


def check_x(base_verb):
    root = ""
    if base_verb[0] == "ا":
        if base_verb[1] == "س":
            if base_verb[2] == "ت":
                root = root + base_verb[3]
                root = root + base_verb[4]
                root = root + base_verb[5]
                return True, root
            else:
                return False, ""
        else:
            return False, ""
    else:
        return False, ""


which_form("استفعل")
