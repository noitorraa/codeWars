def positive_sum(arr):
    return sum(x for x in arr if x > 0)


print(positive_sum([0, 1, -4, 6]))
