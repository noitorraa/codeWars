def pfinten_error(s):
    counter = 0
    for i in s:
        if i not in "abcdifghjklm":
            counter += 1
    return "".join(str(counter) + "/" + str(len(s)))


def pfinten_error_optimized(s):
    return f"{sum(1 for char in s if char not in 'abcdefghijklm')}/{len(s)}"


def test_pfinten_error_case1():
    assert pfinten_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz") == "3/56"


def test_pfinten_error_case2():
    assert pfinten_error("kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz") == "6/60"


def test_pfinten_error_optimized_case1():
    assert (
        pfinten_error_optimized("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz")
        == "3/56"
    )


def test_pfinten_error_optimized_case2():
    assert (
        pfinten_error_optimized(
            "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
        )
        == "6/60"
    )
