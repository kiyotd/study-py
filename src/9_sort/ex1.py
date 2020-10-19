names = ["name1-1980", "name2-1990", "name3-1985"]

# 関数を定義する場合
# def get_year(str_):
#     year = int(str_[-4:])
#     return year
#
#
# names.sort(key=get_year)

# 無名関数で書く場合
names.sort(key=lambda _str: int(_str[-4:]))

print(names)
