# スコアのリスト
scores = [20, 30, 40, 50, 60, 30]


# 渡されたリスト内の合計値を返す
def sum_function(number_list):
    _total = 0
    for number in number_list:
        _total += number
    return _total


# 合計スコア
total_score = sum_function(scores)

# 平均スコア
average_score = total_score / len(scores)

print("total score =", total_score)  # total score = 200
print("average score =", average_score)  # average score = 40
