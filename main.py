# 3 відео: числа і операції над ними
print(3+3, 2-1, 2*4, 4/2, 10//4, 4%2, 4**2)
print(abs(-3))
print(min(6, 8, 3, 6, 2, 7, 5))
print(max(3, 5, 4, 1, 4, 6, 7, 9))
print(pow(3, 3))
print(round(4.6))
print(round(4.56, 1))
# 4 відео: змінні, оператор присвоєння
a = 5
b = a
print(b)
# 5 Ввод вивід, команда input()
c = input()
print(c)
d = int(input())
print(d)
f = float(input())
print(f)
# 6 функція print()
print(1, 2, 3)
print(1, 2, 3, sep=',')
print(1, 2, 3, sep=',', end=' ')
print(4, 5, 6)
q = 50
print("Число", q)
print("Число %s" % q)
# 7 Ділення націло і ділення на остачу
print("Націло:", 3553 // 10, "Остача:", 3553 % 10)
# 8 логічний тип Bool. Операції порівняння
print("3 > 4", 3 > 4)
print("3 < 4", 3 < 4)
print("3 % 3 == 0", 3 % 3 == 0)
print("3 <= 5", 3 <= 5)
print("3 >= 5", 3 >= 5)
print("3 != 2", 3 != 2)
q = 5
w = 4
print(not q % 2 == 0)
print(q > 0 and w > 0)
print(q >= 5 or w >= 5)
# 9 Рядки та операції над ними
z = 'Hello '
x = 'World'
print(z + x)
print(len(z))
print('l' in x)
print(ord('x'))
# 10 Рядки: індекси та зрізи
z = 'Hello World'
print(z[6])
print(z[3:7])
print(z[3:])
print(z[:9])
print(z[:])
print(z[::3])
print(z[::-1])
# 11 Рядки та їх методи
print(z.upper())
print("HELLO".lower())
print(z.count('l'))
print(z.count('l', 3))
print(z.count('l', 3, 6))
print(z.find('o'))
print(z.index('W'))
print(z.replace('o', 'A'))
print("Hello".isalpha())
print("123".isdigit())
s = '111'
print(s.ljust(3, '0'))
print(z.split())
z = z.split()
print('   '.join(z))
e = 'Hello     world'
e.strip()
print(e)
# 12 Списки та операції над ними
r = [1,2,3]
print(len(r))
r = r + [4]
print(r)
r = r * 2
print(r)
print(4 in r)
print(max(r))
print(min(r))
print(sum(r))
print(sorted(r))
print(sorted(r, reverse=True))
print([10, 3, 2] > [9, 8, 77, 80])  # порівнюються перші елементи списку
print([10, 3, 2] == [10, 8, 77, 80])
# 13 Списки: індекси та зрізи
print(r[4])
print(r[-1])
print(r[2:5])
del r[2]
print(r)
r[1] = 100
print(r)
# 14 Списки та їх методи
r.append(50)
print(r)
y = r.copy()
print(y)
r.clear()
print(r)
print(y.count(50))
print(y.index(50))
print(y.index(4, 5))
y.insert(4, 25)
print(y)
print(y.pop())
y.remove(25)
print(y)
y.reverse()
print(y)
y.sort()
print(y)
# 15 умовний оператор if
print("Введіть число")
d = int(input())
if(d % 2 == 0) :
    print("Число парне")
else:
    print("Число не парне")
# 16 Вкладений оператор if
if(d % 2 == 0) :
    if (d > 5) :
        print("+")
    else:
        print("-")
else:
    print("-")
# 16 elif
if(d % 4 == 0):
    print(1)
elif (d % 4 == 1):
    print(2)
elif (d % 4 == 2):
    print(3)
else:
    print(4)
# 17 цикл while
i = 1
while i < 6:
    print(i)
    i = i + 1
# 18
# 19
# 20 Алгоритм Евкліда
a = int(input())
b = int(input())
while a != b:
    if (a > b):
        a = a - b
    else:
        b = b - a
print(a)
# 21
# 22 Інструкція break, continue, else
i = 1
while i <= 5:
    if (i == 5):
        print('break')
        break
    i = i + 1
    if (i < 3):
        print('continue')
        continue
i = 1
while i <= 5:
    print(i)
    i = i + 1
else:
    print('else')
# 23 range
print(list(range(1,20,3)))
# 24 Цикл for
for i in range(4):
    print (i)
# 25 Цикл for списки
a = [1, 5, 10, 15]
for i in a:
    print(i)

for i in range(4):
    print(i, a[i])

# 27
# 28
# 29 вложені списки
a = [[1,2,3], [6,5,4], [9,7,8]]
print(a[1])
print(a[1][0])