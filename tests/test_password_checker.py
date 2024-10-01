import pytest
from lib.password_checker import PasswordChecker


checker = PasswordChecker()

def test_check_good_password():
    assert checker.check("strongPass1") == True

def test_check_bad_password():
    with pytest.raises(Exception) as e:
        checker.check("12345")
    assert str(e.value) == "Invalid password, must be 8+ characters."
