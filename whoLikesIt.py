def likes(names):
    return "".join(
        "no one" + " likes this"
        if len(names) == 0
        else f"{names[0]}" + " likes this"
        if len(names) == 1
        else f"{names[0]} and {names[1]}" + " like this"
        if len(names) == 2
        else f"{names[0]}, {names[1]} and {names[2]}" + " like this"
        if len(names) == 3
        else f"{names[0]}, {names[1]} and {len(names) - 2} others" + " like this"
    )


def likes_optimized(names):
    d = {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} others like this",
    }
    length = len(names)
    return d[min(4, length)].format(*names, others=length - 2)


def test_likes_no_one():
    assert likes([]) == "no one likes this"


def test_likes_one():
    assert likes(["Peter"]) == "Peter likes this"


def test_likes_two():
    assert likes(["Jacob", "Alex"]) == "Jacob and Alex like this"


def test_likes_three():
    assert likes(["Max", "John", "Mark"]) == "Max, John and Mark like this"


def test_likes_four():
    assert likes(["Alex", "Jacob", "Mark", "Max"]) == "Alex, Jacob and 2 others like this"


def test_likes_optimized_no_one():
    assert likes_optimized([]) == "no one likes this"


def test_likes_optimized_one():
    assert likes_optimized(["Peter"]) == "Peter likes this"


def test_likes_optimized_two():
    assert likes_optimized(["Jacob", "Alex"]) == "Jacob and Alex like this"


def test_likes_optimized_three():
    assert likes_optimized(["Max", "John", "Mark"]) == "Max, John and Mark like this"


def test_likes_optimized_four():
    assert likes_optimized(["Alex", "Jacob", "Mark", "Max"]) == "Alex, Jacob and 2 others like this"
