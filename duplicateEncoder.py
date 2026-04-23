def duplicate_encode(word):
    return "".join(")" if word.lower().count(ch) > 1 else "(" for ch in word.lower())


print(duplicate_encode("recede"))
print(duplicate_encode("Success"))
