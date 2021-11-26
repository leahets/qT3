import verb_base_algorithm

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

def test_form1_check():
    basic = verb_base_algorithm.make_word("فعل")
    hollow = verb_base_algorithm.make_word("نام")
    defective = verb_base_algorithm.make_word("بقع")
    formv = verb_base_algorithm.make_word("تعرّف") 
    form2 = verb_base_algorithm.make_word("درّس") 

    assert verb_base_algorithm.check_i(basic) == True
    assert verb_base_algorithm.check_i(hollow) == True
    assert verb_base_algorithm.check_i(defective) == True
    assert verb_base_algorithm.check_i(formv) == False
    assert verb_base_algorithm.check_i(form2) == False

    # then test if every other case fails
    # is this extra?
    assert verb_base_algorithm.check_ii(basic) == False
    assert verb_base_algorithm.check_iii(basic) == False
    assert verb_base_algorithm.check_iv(basic) == False
    assert verb_base_algorithm.check_v(basic) == False
    assert verb_base_algorithm.check_vi(basic) == False
    assert verb_base_algorithm.check_vii(basic) == False
    assert verb_base_algorithm.check_viii(basic) == False
    assert verb_base_algorithm.check_x(basic) == False

    # assert verb_base_algorithm.check_ii(bacis) == False

def test_form2_check():
    basic = verb_base_algorithm.make_word("فعّل")
    assert verb_base_algorithm.check_ii(basic) == True

    assert verb_base_algorithm.check_i(basic) == False
    assert verb_base_algorithm.check_iii(basic) == False
    assert verb_base_algorithm.check_iv(basic) == False
    assert verb_base_algorithm.check_v(basic) == False
    assert verb_base_algorithm.check_vi(basic) == False
    assert verb_base_algorithm.check_vii(basic) == False
    assert verb_base_algorithm.check_viii(basic) == False
    assert verb_base_algorithm.check_x(basic) == False

def test_form3_check():
    basic = verb_base_algorithm.make_word("فاعل")

    assert verb_base_algorithm.check_iii(basic) == True


    assert verb_base_algorithm.check_i(basic) == False
    assert verb_base_algorithm.check_ii(basic) == False
    assert verb_base_algorithm.check_iv(basic) == False
    assert verb_base_algorithm.check_v(basic) == False
    assert verb_base_algorithm.check_vi(basic) == False
    assert verb_base_algorithm.check_vii(basic) == False
    assert verb_base_algorithm.check_viii(basic) == False
    assert verb_base_algorithm.check_x(basic) == False

def test_form4_check():
    basic = verb_base_algorithm.make_word("أفعل")
    assert verb_base_algorithm.check_iv(basic) == True

    assert verb_base_algorithm.check_iii(basic) == False
    assert verb_base_algorithm.check_i(basic) == False
    assert verb_base_algorithm.check_ii(basic) == False
    assert verb_base_algorithm.check_v(basic) == False
    assert verb_base_algorithm.check_vi(basic) == False
    assert verb_base_algorithm.check_vii(basic) == False
    assert verb_base_algorithm.check_viii(basic) == False
    assert verb_base_algorithm.check_x(basic) == False

def test_form5_check():
    basic = verb_base_algorithm.make_word("تفعّل")
    assert verb_base_algorithm.check_v(basic) == True

    assert verb_base_algorithm.check_iii(basic) == False
    assert verb_base_algorithm.check_i(basic) == False
    assert verb_base_algorithm.check_ii(basic) == False
    assert verb_base_algorithm.check_iv(basic) == False
    assert verb_base_algorithm.check_vi(basic) == False
    assert verb_base_algorithm.check_vii(basic) == False
    assert verb_base_algorithm.check_viii(basic) == False
    assert verb_base_algorithm.check_x(basic) == False

def test_form6_check():
    basic = verb_base_algorithm.make_word("تفاعل")
    assert verb_base_algorithm.check_vi(basic) == True

    assert verb_base_algorithm.check_iii(basic) == False
    assert verb_base_algorithm.check_i(basic) == False
    assert verb_base_algorithm.check_ii(basic) == False
    assert verb_base_algorithm.check_iv(basic) == False
    assert verb_base_algorithm.check_v(basic) == False
    assert verb_base_algorithm.check_vii(basic) == False
    assert verb_base_algorithm.check_viii(basic) == False
    assert verb_base_algorithm.check_x(basic) == False

def test_form7_check():
    basic = verb_base_algorithm.make_word("انفعل")
    assert verb_base_algorithm.check_vii(basic) == True

    assert verb_base_algorithm.check_iii(basic) == False
    assert verb_base_algorithm.check_i(basic) == False
    assert verb_base_algorithm.check_ii(basic) == False
    assert verb_base_algorithm.check_iv(basic) == False
    assert verb_base_algorithm.check_v(basic) == False
    assert verb_base_algorithm.check_vi(basic) == False
    assert verb_base_algorithm.check_viii(basic) == False
    assert verb_base_algorithm.check_x(basic) == False

def test_form8_check():
    basic = verb_base_algorithm.make_word("افتعل")
    assert verb_base_algorithm.check_viii(basic) == True

    assert verb_base_algorithm.check_iii(basic) == False
    assert verb_base_algorithm.check_i(basic) == False
    assert verb_base_algorithm.check_ii(basic) == False
    assert verb_base_algorithm.check_iv(basic) == False
    assert verb_base_algorithm.check_v(basic) == False
    assert verb_base_algorithm.check_vi(basic) == False
    assert verb_base_algorithm.check_vii(basic) == False
    assert verb_base_algorithm.check_x(basic) == False

def test_form10_check():
    basic = verb_base_algorithm.make_word("استعمل")
    assert verb_base_algorithm.check_x(basic) == True

    assert verb_base_algorithm.check_iii(basic) == False
    assert verb_base_algorithm.check_i(basic) == False
    assert verb_base_algorithm.check_ii(basic) == False
    assert verb_base_algorithm.check_iv(basic) == False
    assert verb_base_algorithm.check_v(basic) == False
    assert verb_base_algorithm.check_vi(basic) == False
    assert verb_base_algorithm.check_vii(basic) == False
    assert verb_base_algorithm.check_viii(basic) == True

    
def test_which_form_check_if():
    # basic = verb_base_algorithm.make_word("فعّل")
    # assert verb_base_algorithm.which_form(basic) == "Form II", basic
    gibberish = verb_base_algorithm.make_word("ثتصصنيبيت")
    assert verb_base_algorithm.which_form(gibberish) == "Not a verb", gibberish

def test_root():
    basic = verb_base_algorithm.make_word("فعل")

    sample = verb_base_algorithm.make_word("يلعب")

    tricky = verb_base_algorithm.make_word("نام")


    basic1 = verb_base_algorithm.deconjugate(basic)
    basic2 = verb_base_algorithm.strip_fixes(basic1)
    basic_form, basic_value = verb_base_algorithm.which_form(basic2)
    assert basic_value.root == "فعل"

    sample1 = verb_base_algorithm.deconjugate(sample)
    sample2 = verb_base_algorithm.strip_fixes(sample1)
    sample_form, sample_value = verb_base_algorithm.which_form(sample2)
    assert sample_value.root == "لعب"

    tricky1 = verb_base_algorithm.deconjugate(tricky)
    tricky2 = verb_base_algorithm.strip_fixes(tricky1)
    tricky_form, tricky_value = verb_base_algorithm.which_form(tricky2)
    assert tricky_value.root == "نام"


def test_correct_form_basic():
    pass

def test_correct_form():
    #tests form eight and form ten where the leading alif is dropped in all present tense conjugations
    leading_alif_dropped = verb_base_algorithm.make_word("يستعملون")

    leading_alif_dropped = verb_base_algorithm.deconjugate(leading_alif_dropped)
    leading_alif_dropped = verb_base_algorithm.strip_fixes(leading_alif_dropped)
    leading_form, leading_alif_dropped = verb_base_algorithm.which_form(leading_alif_dropped)


    assert leading_form == "Form X"

    leading_alif_dropped1 = verb_base_algorithm.make_word("نقتتل")

    leading_alif_dropped1 = verb_base_algorithm.deconjugate(leading_alif_dropped1)
    leading_alif_dropped1 = verb_base_algorithm.strip_fixes(leading_alif_dropped1)
    leading_form1, leading_alif_dropped1 = verb_base_algorithm.which_form(leading_alif_dropped1)


    assert leading_form1 == "Form VIII"
    # test hamsated verbs like "to eat" where first person form creates double hamsa

    hamsa = verb_base_algorithm.make_word("آكل")

    hamsa = verb_base_algorithm.deconjugate(hamsa)
    hamsa = verb_base_algorithm.strip_fixes(hamsa)
    hamsa_form, hamsa = verb_base_algorithm.which_form(hamsa)

    assert hamsa_form == "Form I"
    assert hamsa.root == "ءكل"
    





#     form, word = verb_base_algorithm.which_form(verb_base_algorithm.deconjugate(basic))
#     assert word.root == "فعل"
#     form, word = verb_base_algorithm.which_form(verb_base_algorithm.deconjugate(sample))
    
#     #shoot we have another ambiguity between form v and form 2


# def test_defective():
#     type1 = verb_base_algorithm.make_word()
    
#     assert verb_base_algorithm.deconjugate()
if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
    #test_form1_check()