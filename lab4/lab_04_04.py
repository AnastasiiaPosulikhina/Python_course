class Encoder:
    def __init__(self, line):
        self.line = line
    def encode(self, line):
        pass
    def decode(self, line):
        pass
    def getCompressionCoef(self, k):
        print("Коэффициент сжатия: ", k)
class HuffmanEncoder(Encoder):
    def __init__(self, compressionCoef):
        Encoder.__init__(self, line)
        self.compressionCoef = compressionCoef
    def encode(self):
        line = self.line
        a = list(line)  # cоздание списка, содержащего строку line
        letters = {}  # словарь для получения списка букв
        for i in range(0, len(a)):  # получение элементов текста файла
            letters[a[i]] = line.count(a[i])
        s = sorted(letters.items(),key=lambda x: x[1])  # отсортированный список, состоящий из встречащихся в файле букв и их количества
        print("Частоты встречающихся в файле элементов: ", s)
        haf = {}  # словарь для кодирования текста методом Хаффмана
        if len(s) == 1:  # условие для случая, когда строка состоит из одного символа
            haf[s[0][0]] = "1"
        if len(s) == 2:  # условие для случая, когда строка состоит из двух символов
            haf[s[0][0]] = "1"
            haf[s[1][0]] = "0"
        while len(s) > 2:  # склеивание наименьших значений элементов словаря и их ключей
            s1 = s[1][0] + s[0][0], s[0][1] + s[1][1]  # объединение двух элементов с наименьшей частотой появления в тексте
            s.insert(0, s1)  # вставка полученного кортежа в список s
            s.remove(s[1])
            s.remove(s[1])
            haf[s[0][0]] = "1"
            x = haf[s[0][0]]  # вспомогательная переменная для кодирования символов
            haf[s[1][0]] = "0"
            x1 = str(s[0][0])  # вспомогательная переменная для кодирования символов
            for i in range(0, len(x1) - 1):
                haf[x1[0]] = x + "0"
                haf[x1[1:]] = x + "1"
                x = haf[x1[1:]]
                x1 = x1[1:]
        haf = sorted(haf.items(), key=lambda x: x[1])  # отсортированный список, представляющий дерево Хаффмана
        res = list()  # список, представляющий закодированный текст
        for i in range(0, len(haf)):
            x2 = str(haf[i][0])
            if len(x2) == 1:
                res.append(haf[i])
        for i in range(0, len(res)):  # кодирование текста
            line = line.replace(res[i][0], res[i][1])
        print("Код для каждого символа: ", res)
        print("Закодированный текст: ", line)
        self.compressionCoef = self.__setCompressionCoef(len(line), len(res)) # осуществление расчёта коэффициента сжатия
        return line, res
    def decode(self, line, encodeHuffman):
        for i in range(len(encodeHuffman) - 1, -1, -1):  # декодирование текста
            line = line.replace(encodeHuffman[i][1], encodeHuffman[i][0])
        print("Декодированный текст: ", line)
    def __setCompressionCoef(self, v1, v2): # осуществление расчёта коэффициента сжатия
        k = v1 / v2
        return k
line = input("Введите строку: ")
enc = HuffmanEncoder(line)
d = enc.encode()
enc.decode(d[0],d[1])
coef = enc._HuffmanEncoder__setCompressionCoef(len(line), len(d[0]))
Encoder.getCompressionCoef(Encoder, coef)
class LZEncoder(Encoder):
    def __init__(self, compressionCoef):
        Encoder.__init__(self, line)
        self.compressionCoef = compressionCoef
    def encode(self):
        line = self.line
        sl = {"": 0}  # словарь для записи ссылок на соответствующие ячейки
        f = []  # список, состоящий из кортежей, необходимый для подготовки словаря sl
        res = ""  # закодированный текст
        ind = ""  # переменная для создания ключей словаря
        for i in range(0, len(line)):  # создание словаря
            ind1 = (ind + line[i]) in sl
            if ind1 is True:  # проверка на наличие ключа в словаре
                ind = ind + line[i]
            else:
                x = sl[ind], line[i]  # создание одного кортежа для списка f (вложение в общий)
                f.append(x)
                sl[ind + line[i]] = len(sl)
                ind = ""
        for i in range(0, len(f)):  # кодирование текста
            for j in range(0, 2):
                res = res + str(f[i][j])
        print("Закодированный текст: ", res)
        print("Словарь: ", sl)
        self.compressionCoef = self.__setCompressionCoef(len(line), len(res)) # осуществление расчёта коэффициента сжатия
        return res
    def decode(self, line):
        text = []  # список, представляющий закодированный текст
        f = []  # список, состоящий из кортежей, для создания списка f1
        f1 = []  # список, состоящий из кортежей, необходимый для подготовки словаря sl
        sl = {'0': ""}  # словарь для записи ссылок на соответствующие ячейки
        res = ""  # декодированный текст
        x = tuple()  # создание одного кортежа для списка
        for i in range(0, len(line)):  # создание списка из закодированного текста
            text.append(line[i])
        for i in text:  # создание списка, состоящего из кортежей, необходимого для подготовки словаря sl
            x = tuple(str(i))
            f.append(x)
        for i in range(0, len(f) - 1, 2):
            y = f[i] + f[i + 1]
            f1.append(y)
        k = 1
        for i in range(0, len(f1)):  # декодирование текста
            plus = sl[f1[i][0]] + f1[i][1]
            res += plus
            sl[str(k)] = plus
            k += 1
        print("Декодированный текст: ", res)
        return res
    def __setCompressionCoef(self, v1, v2): # осуществление расчёта коэффициента сжатия
        k = v1 / v2
        return k
line = input("Введите строку: ")
enc = LZEncoder(line)
d = enc.encode()
enc.decode(d)
coef = enc._LZEncoder__setCompressionCoef(len(line), len(d))
Encoder.getCompressionCoef(Encoder, coef)