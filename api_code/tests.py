import verb_base_algorithm



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
    assert verb_base_algorithm.check_ii(basic) == False
    assert verb_base_algorithm.check_iii(basic) == False
    assert verb_base_algorithm.check_ii(basic) == False

    # assert verb_base_algorithm.check_ii(bacis) == False

def test_form2_check():
    basic = verb_base_algorithm.make_word("فعّل")

    assert verb_base_algorithm.check_ii(basic )

def test_which_form_check_if():
    # basic = verb_base_algorithm.make_word("فعّل")
    # assert verb_base_algorithm.which_form(basic) == "Form II", basic
    gibberish = verb_base_algorithm.make_word("ثتصصنيبيت")
    assert verb_base_algorithm.which_form(gibberish) == "Not a verb", gibberish

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
    #test_form1_check()