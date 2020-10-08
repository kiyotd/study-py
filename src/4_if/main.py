is_login = True
# is_login = False
# is_login = "True"

if is_login and type(is_login) == bool:
    print("You are logged in.")
else:
    print("You are not logged in.")

nums = [0, 1, 2, 3, 4]

# nums に 3 を含むか
if 3 in nums:
    print("nums contains 3")
else:
    print("not include")
