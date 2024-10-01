from lib.report_length import report_length


def test_default_report_length():
    result = report_length("Hello")
    assert result == "This string was 5 characters long."

def test_null_report_length():
    result = report_length("")
    assert result == "This string was 0 characters long."
