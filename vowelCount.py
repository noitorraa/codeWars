def get_count(sentence):
    return sum(sentence.count(v) for v in "aeiou")


print(get_count("aeiouynnjcda"))  # 6
