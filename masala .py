
print('Assalom aleykum\nFizika botga xush kelibsiz\n'
      'Nomalum qismini 0 deb kiriting, marhamat')
s = int(input("masofani kiriting: "))
v = int(input("tezlikni kiriting:"))
t = int(input("vaqtni kiriting:"))


if s and v or v and t or s and t or t and v :
    if s == 0:
        print(v * t)
    elif v == 0:
        print(s / t)
    elif t == 0:
        print(s / v)
    else:
        print('What?')
else:
    print('Fcuk you')
