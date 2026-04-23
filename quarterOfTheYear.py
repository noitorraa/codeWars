def quarter_of(month):
    return (
        1 if 1 <= month <= 3 else 2 if 4 <= month <= 6 else 3 if 7 <= month <= 9 else 4
    )


print(quarter_of(6))
print(quarter_of(8))
print(quarter_of(10))
print(quarter_of(4))
