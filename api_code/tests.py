from typing import final
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
    defective = verb_base_algorithm.make_word("بقى")
    formv = verb_base_algorithm.make_word("تعرّف")
    form2 = verb_base_algorithm.make_word("درّس")

    basic.features.add(verb_base_algorithm.decode_features("r3m1i"))
    hollow.features.add(verb_base_algorithm.decode_features("r3m1i"))
    defective.features.add(verb_base_algorithm.decode_features("r3m1i"))
    formv.features.add(verb_base_algorithm.decode_features("r3f1i"))
    form2.features.add(verb_base_algorithm.decode_features("r3f1i"))

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
    past_features = verb_base_algorithm.decode_features("p2f1n")
    basic.features.add(past_features)
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
    past_features = verb_base_algorithm.decode_features("p2f1n")
    basic.features.add(past_features)
    assert verb_base_algorithm.check_x(basic) == True

    assert verb_base_algorithm.check_iii(basic) == False
    assert verb_base_algorithm.check_i(basic) == False
    assert verb_base_algorithm.check_ii(basic) == False
    assert verb_base_algorithm.check_iv(basic) == False
    assert verb_base_algorithm.check_v(basic) == False
    assert verb_base_algorithm.check_vi(basic) == False
    assert verb_base_algorithm.check_vii(basic) == False
    assert verb_base_algorithm.check_viii(basic) == True


def test_which_form_check_if_gibberish():
    # basic = verb_base_algorithm.make_word("فعّل")
    # assert verb_base_algorithm.which_form(basic) == "Form II", basic
    gibberish = verb_base_algorithm.make_word("ثتصصنيبيت")
    verb_base_algorithm.which_form(gibberish)
    assert gibberish.invalid == True


def test_root():
    basic = verb_base_algorithm.make_word("فعل")

    sample = verb_base_algorithm.make_word("يلعب")

    tricky = verb_base_algorithm.make_word("نام")

    basic1 = verb_base_algorithm.deconjugate(basic)
    basic2 = verb_base_algorithm.strip_fixes(basic1)
    verb_base_algorithm.which_form(basic2)
    assert basic2.root == "ف ع ل"

    sample1 = verb_base_algorithm.deconjugate(sample)
    sample2 = verb_base_algorithm.strip_fixes(sample1)
    verb_base_algorithm.which_form(sample2)
    assert sample2.root == "ل ع ب"

    tricky1 = verb_base_algorithm.deconjugate(tricky)
    # tricky2 = verb_base_algorithm.strip_fixes(tricky1)
    # print(tricky2)
    verb_base_algorithm.which_form(tricky1)
    assert tricky1.root == "ن ا م"


def test_correct_form_basic():
    pass


def test_leading_alif():
    # tests form eight and form ten where the leading alif is dropped in all present tense conjugations
    leading_alif_dropped = verb_base_algorithm.make_word("يستعملون")

    leading_alif_dropped = verb_base_algorithm.deconjugate(
        leading_alif_dropped)

    leading_alif_dropped = verb_base_algorithm.strip_fixes(
        leading_alif_dropped)
    assert leading_alif_dropped.third_past == "ستعمل"
    verb_base_algorithm.which_form(
        leading_alif_dropped)

    assert leading_alif_dropped.form == "Form X"

    leading_alif_dropped1 = verb_base_algorithm.make_word("نقتتل")  # we kill

    leading_alif_dropped1 = verb_base_algorithm.deconjugate(
        leading_alif_dropped1)
    leading_alif_dropped1 = verb_base_algorithm.strip_fixes(
        leading_alif_dropped1)
    verb_base_algorithm.which_form(
        leading_alif_dropped1)

    assert leading_alif_dropped1.form == "Form VIII"


def test_hamsa():
    # test hamsated verbs like "to eat" where first person form creates double hamsa

    hamsa = verb_base_algorithm.make_word("آكل")

    hamsa = verb_base_algorithm.pipeline(hamsa)

    assert hamsa.form == "Form I/Form IV"
    assert hamsa.root == "ء ك ل"

# write a seperate test for form 14 and 25


def test_which_form_raw():
    pass
    # test form 1
    form1 = verb_base_algorithm.make_word("فعل")
    form1.features.add(verb_base_algorithm.decode_features("p3m1n"))
    verb_base_algorithm.which_form(form1)
    assert form1.form == "Form I"

    # test form 2
    form2 = verb_base_algorithm.make_word("فعّل")
    verb_base_algorithm.which_form(form2)
    assert form2.form == "Form II"
    # test form 3
    form3 = verb_base_algorithm.make_word("فاعل")
    verb_base_algorithm.which_form(form3)
    assert form3.form == "Form III"
    # test form 4
    form4 = verb_base_algorithm.make_word("أفعل")
    verb_base_algorithm.which_form(form4)
    assert form4.form == "Form IV"

    # test form 5
    form5 = verb_base_algorithm.make_word("تفعّل")
    verb_base_algorithm.which_form(form5)
    assert form5.form == "Form V"

    # test form 6
    form6 = verb_base_algorithm.make_word("تفاعل")
    verb_base_algorithm.which_form(form6)
    assert form6.form == "Form VI"

    # test form 7
    form7 = verb_base_algorithm.make_word("انفعل")
    verb_base_algorithm.which_form(form7)
    assert form7.form == "Form VII"

    # test form 8
    form8 = verb_base_algorithm.make_word("افتعل")
    past_features = verb_base_algorithm.decode_features("p2f1n")
    form8.features.add(past_features)
    verb_base_algorithm.which_form(form8)
    assert form8.form == "Form VIII"

    # test form 10
    form10 = verb_base_algorithm.make_word("استفعل")
    past_features = verb_base_algorithm.decode_features("p2f1n")
    form10.features.add(past_features)
    verb_base_algorithm.which_form(form10)
    assert form10.form == "Form X"


def test_ambiguous_forms():
    form14 = verb_base_algorithm.pipeline(
        verb_base_algorithm.make_word("أفعل"))
    assert form14.form == "Form I/Form IV"

    form25 = verb_base_algorithm.pipeline(
        verb_base_algorithm.make_word("تدرّس"))
    assert form25.form == "Form II/Form V"

    form5 = verb_base_algorithm.pipeline(
        verb_base_algorithm.make_word("يتدرّس"))
    assert form5.form == "Form V"

    form4 = verb_base_algorithm.pipeline(
        verb_base_algorithm.make_word("يأفعلون"))
    assert form4.form == "Form IV"


def test_full_pipeline():
    pass

    word_list_ex1 = verb_base_algorithm.full_pipeline("فكّت")

    # ex2 =


def test_defective():
    # these words should all be flagged as weak by the algorithm
    ex1 = verb_base_algorithm.full_pipeline("يقضون")

    assert len(ex1) == 1
    word1 = ex1[0]
    assert word1.weak == True
    assert word1.form == "Form I"

    ex2 = verb_base_algorithm.full_pipeline("قضت")

    assert len(ex2) == 1
    word2 = ex2[0]
    assert word2.weak == True
    assert word2.form == "Form I"

    ex3 = verb_base_algorithm.full_pipeline("قضوا")

    assert len(ex3) == 1
    word3 = ex3[0]
    assert word3.weak == True
    assert word3.form == "Form I"

    # these words should all return the root with an alif maqsooora

    #ex4 = full_pipeline("")

    # these words should all return the root with a ya

    #ex4 = full_pipeline("")

    #ex4 = full_pipeline("")

    #ex4 = full_pipeline("")

    # every present tense conjugation


def test_weak_check():
    assimilated_text = "وصل"
    hollow_text = "نام"
    defective_text = "بقى"

    assimilated_list = verb_base_algorithm.full_pipeline(assimilated_text)

    assert len(assimilated_list) == 1
    assert assimilated_list[0].weak == True
    # we have no marker for assimilated - should we?

    hollow_list = verb_base_algorithm.full_pipeline(hollow_text)
    assert len(hollow_list) == 1
    assert hollow_list[0].weak == True
    assert hollow_list[0].hollow == True

    defective_list = verb_base_algorithm.full_pipeline(defective_text)
    assert len(defective_list) == 1
    assert defective_list[0].weak == True
    assert defective_list[0].defective == True


def test_hollow():
    pass


def test_assimilated():
    pass


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

    # test first person second form
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


def test_ending_root_letters():
    final_meem = verb_base_algorithm.make_word("ينام")
    final_meem = verb_base_algorithm.pipeline(final_meem)
    assert final_meem.root == "ن ا م"
    meem_features = final_meem.features
    m_ft1 = verb_base_algorithm.decode_features("r3m1i")
    m_ft2 = verb_base_algorithm.decode_features("r3m1j")
    m_ft3 = verb_base_algorithm.decode_features("r3m1j")
    assert len(meem_features) == 3
    assert m_ft1 in meem_features
    assert m_ft2 in meem_features
    assert m_ft3 in meem_features
    assert final_meem.form == "Form I/Form IV"


def test_all_conjugations_present():
    fake_r1n1i = verb_base_algorithm.make_word(
        "أأخم")  # ahem #this imight be failing
    fake_r1n1i = verb_base_algorithm.deconjugate(fake_r1n1i)
    #assert len(fake_r1n1i.features) == 3
    fake_r1n3i = verb_base_algorithm.make_word("نأخم")
    fake_r1n3i = verb_base_algorithm.deconjugate(fake_r1n3i)
    assert len(fake_r1n3i.features) == 3
    # skip the other one (m) cause it is same as r3f1i
    fake_r2n1i = verb_base_algorithm.make_word("تأخمين")
    fake_r2n1i = verb_base_algorithm.deconjugate(fake_r2n1i)
    assert len(fake_r2n1i.features) == 1
    fake_r2m1i = verb_base_algorithm.make_word("تأخم")
    fake_r2m1i = verb_base_algorithm.deconjugate(fake_r2m1i)
    assert len(fake_r2m1i.features) == 6
    fake_r2n2i = verb_base_algorithm.make_word("تأخمان")
    fake_r2n2i = verb_base_algorithm.deconjugate(fake_r2n2i)
    assert len(fake_r2n2i.features) == 3
    fake_r2n3i = verb_base_algorithm.make_word("تأخمون")
    fake_r2n3i = verb_base_algorithm.deconjugate(fake_r2n3i)
    assert len(fake_r2n3i.features) == 1
    fake_r3m1i = verb_base_algorithm.make_word("يأخم")
    fake_r3m1i = verb_base_algorithm.deconjugate(fake_r3m1i)
    assert len(fake_r3m1i.features) == 3
    # fake_r3f1i = verb_base_algorithm.make_word("تأخم")
    # fake_r3f1i =verb_base_algorithm.make_word(fake_r3f1i)
    # fake_r3f2i = verb_base_algorithm.make_word("")
    # fake_r3m2i = verb_base_algorithm.make_word("")
    fake_r3n3i = verb_base_algorithm.make_word("يأخمون")
    fake_r3n3i = verb_base_algorithm.deconjugate(fake_r3n3i)
    assert len(fake_r3n3i.features) == 1


def test_new_hash():
    # tests feature equality
    f1 = verb_base_algorithm.decode_features("p1n1n")
    f1a = verb_base_algorithm.decode_features("p1n1n")
    f2 = verb_base_algorithm.decode_features("p1f1n")
    assert f1 == f1a
    assert f1 != f2

# def test_defective():
#     type1 = verb_base_algorithm.make_word()


def test_hollow_full():
    word_list = verb_base_algorithm.full_pipeline("باعه")
    word = word_list.pop()
    if word.raw_text == "باعه":
        word = word_list.pop()
    assert word.raw_text == "باع"
    assert word.conjugated == "باع"
    features = word.features.pop()
    assert verb_base_algorithm.decode_features("p3m1n") == features
    assert word.third_past == "باع"
    assert 1 in word.checked_forms
    assert word.root == "ب و/ي ع"
    assert word.form == "Form I"
    assert word.prefix_count == 0  # for conjugations
    assert word.suffix_count == 0  # for conjugations
    assert len(word.possible_prefixes) == 0
    #assert word.suffix == ("ه", "him")
    assert word.future == False
    assert word.weak == True
    assert word.invalid == False
    assert word.dropped_prefixes == []
    assert ("ه", "him") in word.dropped_suffix
    assert word.hollow == True
    assert word.defective == False
    assert word.geminated == False


def test_hollow_full_2():
    word_list = verb_base_algorithm.full_pipeline("صامت")
    word = word_list.pop()
    # if word.raw_text == "صامت":
    #word = word_list.pop()
    assert word.raw_text == "صامت"
    assert word.conjugated == "صامت"
    features = word.features.pop()
    if verb_base_algorithm.decode_features("p3f1n") == features:
        assert verb_base_algorithm.decode_features("p3f1n") == features
    elif verb_base_algorithm.decode_features("p1n1n") == features:
        assert verb_base_algorithm.decode_features("p1n1n") == features
    else:
        assert False == True  # this should never run
    assert word.third_past == "صام"
    assert 1 in word.checked_forms
    assert word.root == "ص و/ي م"
    assert word.form == "Form I"
    assert word.prefix_count == 0  # for conjugations
    assert word.suffix_count == 1  # for conjugations
    assert len(word.possible_prefixes) == 0
    #assert word.suffix == ("ه", "him")
    assert word.future == False
    assert word.weak == True
    assert word.invalid == False
    assert word.dropped_prefixes == []
    # assert ("ه", "him") in word.dropped_suffix
    assert word.hollow == True
    assert word.defective == False
    assert word.geminated == False


def test_assimilated_full():
    word_list = verb_base_algorithm.full_pipeline("وصل")
    word = word_list.pop()
    assert word.raw_text == "وصل"
    assert word.conjugated == "وصل"
    features = word.features.pop()
    assert verb_base_algorithm.decode_features("p3m1n") == features
    assert word.third_past == "وصل"
    assert 1 in word.checked_forms
    assert word.root == "و ص ل"
    assert word.form == "Form I"
    assert word.prefix_count == 0  # for conjugations
    assert word.suffix_count == 0  # for conjugations
    assert len(word.possible_prefixes) == 0
    #assert word.suffix == ("ه", "him")
    assert word.future == False
    assert word.weak == True
    assert word.invalid == False
    assert word.dropped_prefixes == []
    assert len(word.dropped_suffix) == 0
    assert word.hollow == False
    assert word.defective == False
    assert word.geminated == False


def test_assimilated_dropped():
    word_list = verb_base_algorithm.full_pipeline("يصل")
    word = word_list.pop()
    assert word.raw_text == "يصل"
    assert word.conjugated == "يصل"
    features = word.features.pop()
    if verb_base_algorithm.decode_features("r3m1i") == features:
        assert verb_base_algorithm.decode_features("r3m1i") == features
    elif verb_base_algorithm.decode_features("r3m1s") == features:
        assert verb_base_algorithm.decode_features("r3m1s") == features
    elif verb_base_algorithm.decode_features("r3m1j") == features:
        assert verb_base_algorithm.decode_features("r3m1j") == features
    else:
        assert False == True  # this should never run
    assert word.third_past == "صل"
    assert 1 in word.checked_forms
    assert word.root == "و/ي ص ل"
    assert word.form == "Form I"
    assert word.prefix_count == 1  # for conjugations
    assert word.suffix_count == 0  # for conjugations
    assert len(word.possible_prefixes) == 0
    #assert word.suffix == ("ه", "him")
    assert word.future == False
    assert word.weak == True
    assert word.invalid == False
    assert word.dropped_prefixes == []
    assert len(word.dropped_suffix) == 0
    assert word.hollow == False
    assert word.defective == False
    assert word.geminated == False


def test_defective_full():
    pass


#     assert verb_base_algorithm.deconjugate()
if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
    # test_form1_check()
