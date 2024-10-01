from lib.gratitudes import Gratitudes


def test_gratitudes_format():
    gratitudes = Gratitudes()
    gratitudes.add("Food")
    gratitudes.add("Water")
    assert gratitudes.format() == "Be grateful for: Food, Water"
