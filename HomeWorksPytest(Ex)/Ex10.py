def test_pytest():
    phrase = input("Set a phrase: ")
    assert len(phrase) <= 15, 'Error, phrase length more than 15 characters'

