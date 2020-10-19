def to_double(num):
    return num * 2


nums = [1, 2, 3, 4, 5]
for cm in map(to_double, nums):
    print(cm)
