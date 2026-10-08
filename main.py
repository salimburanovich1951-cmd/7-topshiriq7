#ismlar=["Ali","Vali","Elbek","Bobur","Asadbek"]
#print(ismlar)
#for ism in ismlar:
 #print("salom",ism)
sonlar = list(range(11, 101, 2))
for son in sonlar:
    print(son ** 3)
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car == "gm":
        print(car.upper())
    else:
        print(car.title())
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car != "gm":
     print(car.title())
else:
    print(car.upper())
login = input("Loginni kiriting: ")
if login == "admin":
    print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print(f"Xush kelibsiz, {login}!")
a = input("1-sonni kiriting: ")
b = input("2-sonni kiriting: ")
if a == b:
    print("Sonlar teng")
    son =int(input("Son kiriting: "))
    if son < 0:
        print("Manfiy son")
    else:
        print("Musbat son")
    son = int(input("Son kiriting: "))
    if son < 0:
        print("Manfiy son")
    else:
        print("Musbat son")
    son = int(input("Son kiriting: "))
    if son >= 0:
        print(son ** 0.5)
    else:
        print("Musbat son kiriting")
