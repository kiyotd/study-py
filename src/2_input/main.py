print("整数2つで足し算を行います。")

num1 = input("1つ目の数を入力してください：")
num2 = input("2つ目の数を入力してください：")

# int型にキャストして計算
calc = int(num1) + int(num2)

# str型にキャストして出力
print("答えは " + str(calc) + " です。")
