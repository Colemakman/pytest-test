import pytest
from lib.password_checker import PasswordChecker


checker = PasswordChecker()

def check_good_password():
    assert checker.check("strongPass1") == True

def check_bad_password():
    with pytest.raises(Exception) as e:
        checker.check("12345")
    assert str(e.value) == "Invalid password, must be 8+ characters."
