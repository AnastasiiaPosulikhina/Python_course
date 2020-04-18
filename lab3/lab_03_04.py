'''
Словари
'''
d1 = {"day": 18, "month": 6, "year": 1983}
print(list(d1.values()))
print(list(d1))
d2 = dict(bananas=3,apples=5,oranges=2,bag="basket")
d3 = dict([("street","Kronverksky pr."), ("house", 49)])
d4 = dict.fromkeys(["1","2"], 3)
print("Dict d1 = ", d1)
print("Dict d2 by dict()= ", d2)
print("Dict d3 by dict([])= ", d3)
print("Dict d4 by fromkeys = ", d4)
print("\n")
'''
Дополнение кода программы
'''
startDict1 = {"ready": 3, "set": 2, "go": 1}
startDict2 = dict(ready = 3,set = 2,go = 1)
startDict3 = dict([("ready", 3), ("set", 2), ("go", 1)])
print("Dict startDict1 = ", startDict1)
print("Dict startDict2 = ", startDict2)
print("Dict startDict3 = ", startDict3)
dict1 = dict.fromkeys(["key1","key2"], input("Введите ключ: "))
print("Dict1 = ", dict1)
