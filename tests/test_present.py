import pytest
from lib.present import Present


def test_empty_present():
    p = Present()
    with pytest.raises(Exception) as e:
        p.unwrap()
    assert str(e.value) == "No contents have been wrapped."

def test_already_unwrapped_present():
    p = Present()
    p.wrap("Bongo")
    with pytest.raises(Exception) as e:
        p.wrap("Flute")
    assert str(e.value) == "A contents has already been wrapped."

def test_default_present():
    p = Present()
    p.wrap("Guitar")
    assert p.unwrap() == "Guitar"
