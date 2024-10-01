from lib.greet import greet


def test_greet_with_name():
    result = greet("Bim")
    assert result == "Hello, Bim"
