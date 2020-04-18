'''
Множества
'''
# создание множества
b1 = set()
print("Set b1 = ", b1)
b2 = {"bear", "fox", "squirrel", "woodpecker", "woodpecker", "wolf", "hedgehog"}
print("Set b2 = ", b2)
# создание множества из строки
b3 = set("abcdabcdefg")
print("Set b3 from string: ", set(b3))
print("\n")
'''
Дополнение кода программы
'''
s = "Electricity is the set of physical phenomena associated with the presence of electric charge. Lightning is one of the most dramatic effects of electricity."
set1 = set(s)
print("set1 = ", set1)
for i in range(1):
    if "a" in set1:
        print("a", end=" ")
    if "E" in set1:
        print("E", end=" ")
    if "e" in set1:
        print("e", end=" ")
    if "i" in set1:
        print("i", end=" ")
    if "o" in set1:
        print("o", end=" ")
    if "u" in set1:
        print("u", end=" ")
    if "y" in set1:
        print("y", end=" ")