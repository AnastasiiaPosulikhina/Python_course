fileIn = open("fileIn.txt", 'r') # открытие файла fileIn для чтения
fileOut = open("fileOut.txt", 'w') # открытие файла fileOut для записи с перезаписью размещённых ранее данных
fileOut2 = open("fileOut2.txt", 'w') # открытие файла fileOut2 для записи с перезаписью размещённых ранее данных
sravnenie = str(fileIn.read()) # переменная, хранящая в себе исходный текст файла
fileIn.close()
fileIn = open("fileIn.txt", 'r')
print("Кодирование и декодирование текста с использованием метода Хаффмана")
def encodeHuffman(fileIn, fileOut):
    line = fileIn.read()  # чтение данных из файла fileIn
    a = list(line)  # cоздание списка, содержащего строку line
    letters = {} # словарь для получения списка букв
    for i in range(0, len(a)): # получение элементов текста файла
        letters[a[i]] = line.count(a[i])
    s = sorted(letters.items(), key=lambda x: x[1]) # отсортированный список, состоящий из встречащихся в файле букв и их количества
    print("Частоты встречающихся в файле элементов: ", s)
    haf = {} # словарь для кодирования текста методом Хаффмана
    if len(s) == 1: # условие для случая, когда строка состоит из одного символа
        haf[s[0][0]] = "1"
    if len(s) == 2: # условие для случая, когда строка состоит из двух символов
        haf[s[0][0]] = "1"
        haf[s[1][0]] = "0"
    while len(s) > 2:  # склеивание наименьших значений элементов словаря и их ключей
        s1 = s[1][0] + s[0][0], s[0][1] + s[1][1] # объединение двух элементов с наименьшей частотой появления в тексте
        s.insert(0, s1) #  вставка полученного кортежа в список s
        s.remove(s[1])
        s.remove(s[1])
        haf[s[0][0]] = "1"
        x = haf[s[0][0]] # вспомогательная переменная для кодирования символов
        haf[s[1][0]] = "0"
        x1 = str(s[0][0]) # вспомогательная переменная для кодирования символов
        for i in range(0, len(x1) - 1):
            haf[x1[0]] = x + "0"
            haf[x1[1:]] = x + "1"
            x = haf[x1[1:]]
            x1 = x1[1:]
    haf = sorted(haf.items(), key=lambda x: x[1]) # отсортированный список, представляющий дерево Хаффмана
    res = list() # список, представляющий закодированный текст
    for i in range(0, len(haf)):
        x2 = str(haf[i][0])
        if len(x2) == 1:
            res.append(haf[i])
    for i in range(0, len(res)): # кодирование текста
        line = line.replace(res[i][0], res[i][1])
    print("Код для каждого символа: ", res)
    print("Закодированный текст: ", line)
    fileOut.write(line)
    return res
encodeHuffman1 = encodeHuffman(fileIn, fileOut)
fileOut = open("fileOut.txt", 'r+')
def decodeHuffman(fileIn, fileOut, encodeHuffman1):
    line = fileIn.read() # чтение теста исходного файла
    for i in range(len(encodeHuffman1) - 1, -1, -1): # декодирование текста
        line = line.replace(encodeHuffman1[i][1], encodeHuffman1[i][0])
    fileOut2.write(line)
    print("Декодированный текст: ", line)
    fileIn = open("fileIn.txt", 'r')
    if sravnenie == line: # проверка на возникновение ошибок в работе программы
        print("True")
    else:
        print("False")
decodeHuffman(fileOut, fileOut2, encodeHuffman1)

print("\nКодирование и декодирование текста с использованием метода Лемпеля-Зива")
fileOut = open("fileOut1.txt", 'w') # открытие файла fileOut1 для записи
def encodeLZ(fileIn, fileOut):
    fileIn = open("fileIn.txt", 'r')
    line = fileIn.read() # чтение данных из файла fileIn
    sl = {"": 0} # словарь для записи ссылок на соответствующие ячейки
    f = [] # список, состоящий из кортежей, необходимый для подготовки словаря sl
    res= "" # закодированный текст
    ind = "" # переменная для создания ключей словаря
    for i in range(0, len(line)): # создание словаря
        ind1 = (ind + line[i]) in sl
        if ind1 is True: # проверка на наличие ключа в словаре
            ind = ind + line[i]
        else:
            x = sl[ind], line[i] # создание одного кортежа для списка f (вложение в общий)
            f.append(x)
            sl[ind + line[i]] = len(sl)
            ind = ""
    for i in range(0, len(f)): # кодирование текста
        for j in range(0, 2):
            res = res + str(f[i][j])
    fileOut.write(res)
    print("Закодированный текст: ", res)
    print("Словарь: ",sl)
    fileOut.close()
    return sl
fileOut = open("fileOut1.txt", 'w')
def decodeLZ(fileIn, fileOut):
    line = fileIn.read() # чтение данных из файла fileIn
    text = [] # список, представляющий закодированный текст
    f = [] # список, состоящий из кортежей, для создания списка f1
    f1 = [] # список, состоящий из кортежей, необходимый для подготовки словаря sl
    sl = {'0': ""} # словарь для записи ссылок на соответствующие ячейки
    res = ""  # декодированный текст
    x = tuple() # создание одного кортежа для списка
    for i in range(0, len(line)): # создание списка из закодированного текста
        text.append(line[i])
    for i in text: # создание списка, состоящего из кортежей, необходимого для подготовки словаря sl
        x = tuple(str(i))
        f.append(x)
    for i in range(0, len(f)-1,2):
        y = f[i] + f[i+1]
        f1.append(y)
        print(f1)
    k = 1
    for i in range(0, len(f1)): # декодирование текста
        plus = sl[f1[i][0]] + f1[i][1]
        res += plus
        sl[str(k)] = plus
        k += 1
    fileOut.write("\n\n")
    fileOut.write(res)
    print("Декодированный текст: ", res)
    if sravnenie == res:  # проверка на возникновение ошибок в работе программы
        print("True")
    else:
        print("False")
    return res
encodeLZ(fileIn, fileOut)
fileOut = open("fileOut1.txt", 'r+')
decodeLZ(fileOut, fileOut2)

print("\nПодсчёт коэффициентов сжатия текстов")
# Текст для кодирования методом Хаффмана: ok
# Текст для кодирования методом Лемпеля-Зива: aaaaaaaaabaaacaaabdaabffffff
fileIn = open("fileIn.txt", 'r')
fileOut = open("fileOut.txt", 'r+')
fileOut1 = open("fileOut1.txt", 'r+')
v1 = len(fileIn.read())
v2 = len(fileOut.read())
v3 = len(fileOut1.read())
print("Объём исходных данных: ", v1)
print("Объём сжатых по методу Хаффмана данных: ", v2)
print("Коэффициент сжатия: %.5f" % (v1 / v2))
print("Объём сжатых по методу Лемпеля-Зива данных: ", v3)
print("Коэффициент сжатия: {}".format(v1 / v3))