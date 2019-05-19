import minifb

n = input("name: ")
p = input("pass: ")

u = minifb.LogIn(n,p)
if u:
    print("login!")
    mes,pub = u.newContent()
    print(len(mes), len(pub))

else:
    print("fail login")
