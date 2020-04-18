import itertools
s = input("Введите строку: ")
print(set((itertools.permutations(list(s)))))
