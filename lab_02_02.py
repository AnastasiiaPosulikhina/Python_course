'''
Циклы
'''
# while
print("Numbers < 10 (while):")
i = 0
while (i<10):
    print(i, end=" ") # print in one line
    i += 1
print("\n")
# for
print("Numbers < 10 (for):")
for i in range(0,10):
    print(i, end=" ")
else:
    print("\nThe next number is 10\n")
# break
sum = 0
for i in range(0,100):
    if i > 10:
        print("\nWe reached the end, final sum: ", sum)
        break
    sum += i
# continue
i = 0
while i<=15:
    if i % 3 == 0:
        i += 1
        continue
    print(i, end=" ")
    i += 1
print("\n")
# pass
print("Let's print numbers again!")
for i in range(0,10):
    pass
    print(i, end=" ")
print("\n\n")
'''
 Дополнение кода программы
'''
print("Числа от 0 до 500, делящиеся на 7: ")
for i in range (0, 501):
    if i % 7 == 0: # условие кратности 7-и
        print(i, end=" ")
print("\n")
i = 0
while (i<501):
    if (i % 7 == 0) and (i % 14 !=0 ): # условие кратности 7-и и не кратности 14-ти
        print(i, end=" ")
    i += 1
    if i >= 300:
        print("\nAll numbers were printed!")
        break
j = 1 # переменная, организующая вывод каждой новой строки таблицы
for k in range (1,17):
    if (k%5 == 1):
        print(j//5+1, end=' ')
    else:
        print (0, end =' ')
    if (j%4 == 0): # цикл, организующий переход на новую строку таблицы
        print("\n")
    j += 1
print("\n")
j1 = 1
k1 = 1
while k1 < 17:
    if (k1%5 == 1):
        print(j1//5+1, end=' ')
    else:
        print (0, end =' ')
    if (j1%4 == 0):
        print("\n")
    j1 += 1
    k1 += 1

a1 =[]
for i in range (0,20):
    if i % 3 ==0:
        a1.append(3)
    else:
        a1.append(0)
a1.sort(reverse= True)
a1.pop(0)
print(a1)






