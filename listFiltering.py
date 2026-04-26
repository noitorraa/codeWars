def filter_list(l):
    return [i for i in l if isinstance(i, int)]


def test_filter_list():
    assert filter_list([1, 12, "kf3", 8, "12", 5, "te", 2, -4]) == [1, 12, 8, 5, 2, -4]
