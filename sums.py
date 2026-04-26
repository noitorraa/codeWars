def positive_sum(arr):
    return sum(x for x in arr if x > 0)


def test_positive_sum():
    assert positive_sum([0, 1, -4, 6]) == 7
