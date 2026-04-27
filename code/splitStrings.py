def solution(s):
    dictionary = [
        s[i : i + 2] if i + 2 <= len(s) else s[i:] + "_" for i in range(0, len(s), 2)
    ]
    return dictionary


def test_solution():
    assert solution("adakdmekfemadcwec") == ['ad', 'ak', 'dm', 'ek', 'fe', 'ma', 'dc', 'we', 'c_']
