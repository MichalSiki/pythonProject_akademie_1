uzivatele = ("bob", "ann", "mike", "liz")
password_n = ("123", "pass123", "password123", "pass123")

username = input("Zadej jmeno: ")
password = input("Zadej heslo: ")
print("username: ", username)
print("password: ", password)

if username in uzivatele and password in password_n:
    print("Jmeno a heslo je správné")
else:
    print("Zadej správné jméno a heslo")
