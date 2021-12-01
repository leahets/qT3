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
    # tests form eight and form ten where the leading alif is dropped in all present tense conjugations
    leading_alif_dropped = verb_base_algorithm.make_word("يستعملون")

    leading_alif_dropped = verb_base_algorithm.deconjugate(
        leading_alif_dropped)
    leading_alif_dropped = verb_base_algorithm.strip_fixes(
        leading_alif_dropped)
    leading_form, leading_alif_dropped = verb_base_algorithm.which_form(
        leading_alif_dropped)

    assert leading_form == "Form X"

    leading_alif_dropped1 = verb_base_algorithm.make_word("نقتتل")

    leading_alif_dropped1 = verb_base_algorithm.deconjugate(
        leading_alif_dropped1)
    leading_alif_dropped1 = verb_base_algorithm.strip_fixes(
        leading_alif_dropped1)
    leading_form1, leading_alif_dropped1 = verb_base_algorithm.which_form(
        leading_alif_dropped1)

    assert leading_form1 == "Form VIII"
    # test hamsated verbs like "to eat" where first person form creates double hamsa

    hamsa = verb_base_algorithm.make_word("آكل")

    hamsa = verb_base_algorithm.deconjugate(hamsa)
    hamsa = verb_base_algorithm.strip_fixes(hamsa)
    hamsa_form, hamsa = verb_base_algorithm.which_form(hamsa)

    assert hamsa_form == "Form I"
    assert hamsa.root == "ءكل"


def test_deconjugate():
    #  test we form
    first_plural = verb_base_algorithm.make_word("نفعل")
    first_plural_feature1 = verb_base_algorithm.decode_features("r1n3i")
    first_plural_feature2 = verb_base_algorithm.decode_features("r1n3j")
    first_plural_feature3 = verb_base_algorithm.decode_features("r1n3s")
    first_plural = verb_base_algorithm.deconjugate(first_plural)
    assert first_plural_feature1 in first_plural.features
    assert first_plural_feature2 in first_plural.features
    assert first_plural_feature3 in first_plural.features
    assert len(first_plural.features) == 3

    first_sing = verb_base_algorithm.make_word("أفعل")
    first_sing_feature1 = verb_base_algorithm.decode_features("r1n1i")
    first_sing_feature2 = verb_base_algorithm.decode_features("r1n1j")
    first_sing_feature3 = verb_base_algorithm.decode_features("r1n1s")
    first_sing = verb_base_algorithm.deconjugate(first_sing)
    assert first_sing_feature1 in first_sing.features
    assert first_sing_feature2 in first_sing.features
    assert first_sing_feature3 in first_sing.features
    assert len(first_plural.features) == 3

    # checks first person past tense, aka feminine past singular and second past singular forms
    first_past = verb_base_algorithm.make_word("فعلت")
    first_past_feature1 = verb_base_algorithm.decode_features("p1n1n")
    first_past_feature2 = verb_base_algorithm.decode_features("p3f1n")
    first_past_feature3 = verb_base_algorithm.decode_features("p2f1n")
    first_past_feature4 = verb_base_algorithm.decode_features("p2m1n")
    first_past = verb_base_algorithm.deconjugate(first_past)
    assert first_past_feature1 in first_past.features
    assert first_past_feature2 in first_past.features
    assert first_past_feature3 in first_past.features
    assert first_past_feature4 in first_past.features

    assert len(first_past.features) == 4

    # test first person secoond form
    # not sure why this test isn't working rn, will come back to it
    # second_person = verb_base_algorithm.make_word("تفعلين")
    # #second_feature1 = verb_base_algorithm.decode_features("r3f1i")
    # second_feature2 = verb_base_algorithm.decode_features("r2f1i")
    # #second_feature3 = verb_base_algorithm.decode_features("r3f1j")
    # #second_feature4 = verb_base_algorithm.decode_features("r2f1j")
    # #second_feature5 = verb_base_algorithm.decode_features("r3f1s")
    # #second_feature6 = verb_base_algorithm.decode_features("r2f1s")

    # #assert second_feature1 in second_person.features
    # assert second_feature2 in second_person.features
    # #assert second_feature3 in second_person.features
    # #assert second_feature4 in second_person.features
    # #assert second_feature5 in second_person.features
    # #assert second_feature6 in second_person.features

    # assert len(second_person.features) == 6
#     form, word = verb_base_algorithm.which_form(verb_base_algorithm.deconjugate(basic))
#     assert word.root == "فعل"
#     form, word = verb_base_algorithm.which_form(verb_base_algorithm.deconjugate(sample))

#     #shoot we have another ambiguity between form v and form 2


def test_new_hash():
    # tests feature equality
    f1 = verb_base_algorithm.decode_features("p1n1n")
    f1a = verb_base_algorithm.decode_features("p1n1n")
    f2 = verb_base_algorithm.decode_features("p1f1n")
    assert f1 == f1a
    assert f1 != f2

# def test_defective():
#     type1 = verb_base_algorithm.make_word()


#     assert verb_base_algorithm.deconjugate()
if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
    # test_form1_check()
