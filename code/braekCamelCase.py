def solution(s):
    result = ""
    for i in s:
        result += "".join((" " + i) if i.isupper() else i)
    return result


def solution_alternative(s):
    return "".join(" " + c if c.isupper() else c for c in s)


def test_solution_hello_world():
    assert solution("helloWorld") == "hello World"


def test_solution_braek_camel_case():
    assert solution("braekCamelCase") == "braek Camel Case"


def test_solution_alternative_hello_world():
    assert solution_alternative("helloWorld") == "hello World"


def test_solution_alternative_braek_camel_case():
    assert solution_alternative("braekCamelCase") == "braek Camel Case"
