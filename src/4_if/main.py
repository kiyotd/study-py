is_login = True
# is_login = False
# is_login = "True"

if is_login and type(is_login) == bool:
    print("You are logged in.")
else:
    print("You are not logged in.")
