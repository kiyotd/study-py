list_ = [0, 1, 2, 3, 4]
tuple_ = (0, 1, 2, 3, 4)

print(list_)  # [0, 1, 2, 3, 4]
print(tuple_)  # (0, 1, 2, 3, 4)

# *
# unpack 展開する
print(*list_)  # 0 1 2 3 4
print(*tuple_)  # 0 1 2 3 4

# **
# 辞書などをキーワード引数として渡すことができる
my_dict = {"sep": " / "}
print(1, 2, 3, **my_dict)  # 1 / 2 / 3
print(1, 2, 3, sep=" / ")  # と同じ


# 関数を定義するとき
# 与えられた実引数はタプルにまとめられる
def sum_func(*nums):
    total_ = 0
    for num in nums:
        total_ += num
    return total_


print(sum_func(1, 2, 3, 4, 5))  # 15
