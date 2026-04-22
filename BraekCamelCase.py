def solution(s):
    result = ""
    for i in s:
        result += "".join((" " + i) if i.isupper() else i)
    return result


def solution_alternative(s):
    return "".join(" " + c if c.isupper() else c for c in s)


print(solution("helloWorld"))
print(solution("braekCamelCase"))
