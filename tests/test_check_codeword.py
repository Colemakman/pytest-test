from lib.check_codeword import check_codeword


def test_check_correct_codeword():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_check_close_codeword():
    result = check_codeword("house")
    assert result == "Close, but nope."

def test_check_wrong_codeword():
    result = check_codeword("cheese")
    assert result == "WRONG!"


