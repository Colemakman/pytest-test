from lib.counter import Counter


def test_default_counter():
    counter = Counter()
    counter.add(3)
    counter.add(2)
    assert counter.report() == "Counted to 5 so far."
