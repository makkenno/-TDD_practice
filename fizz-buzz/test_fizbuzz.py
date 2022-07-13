from fizzbuzz import fizzbuzz


def test_fizzbuzz():
    assert fizzbuzz(3) == 'fizz'
    assert fizzbuzz(5) == 'buzz'
    assert fizzbuzz(6) == 'fizz'
    assert fizzbuzz(4) == 4
    assert fizzbuzz(15) == 'fizzbuzz'
