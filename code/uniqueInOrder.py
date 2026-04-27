def unique_in_order(sequence):
    result = []
    for item in sequence:
        if not result or item != result[-1]:
            result.append(item)
    return result


def test_unique_in_order_string():
    assert unique_in_order("AAAABBBCCDAABBB") == ['A', 'B', 'C', 'D', 'A', 'B']


def test_unique_in_order_list():
    assert unique_in_order(
        [1, 2, 3, 3, -1, "4s", "4s", "4s", "fds", 3, 3, 3, 3, "6bbs", "4s", "B"]
    ) == [1, 2, 3, -1, "4s", "fds", 3, "6bbs", "4s", "B"]
