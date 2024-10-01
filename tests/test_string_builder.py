from lib.string_builder import StringBuilder


def test_string_bulider_size():
    string = StringBuilder()
    string.add("Hello, ")
    string.add("World!")
    assert string.size() == 13

def test_string_builder_output():
    string = StringBuilder()
    string.add("Hello, ")
    string.add("World!")
    assert string.output() == "Hello, World!"
