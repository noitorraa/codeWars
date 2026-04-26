def pig_it(text):
    words = text.split()
    for i in range(len(words)):
        if words[i].isalpha():
            words[i] = words[i][1:] + words[i][0] + "ay"
    return " ".join(words)


def pig_it_optimized(text):
    return " ".join(
        word[1:] + word[0] + "ay" if word.isalpha() else word for word in text.split()
    )


def test_pig_it():
    assert pig_it("Pig latin is cool") == "igPay atinlay siay oolcay"


def test_pig_it_optimized():
    assert pig_it_optimized("Pig latin is cool") == "igPay atinlay siay oolcay"
