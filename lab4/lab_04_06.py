import math
class HammingEncoder:
    def __init__(self, dataBits):
        self.dataBits = dataBits
        for i in range(0, 10):
            if 2 ** i >= dataBits + 1 + i:
                self.controlBits = i
                break
        print("Количество контрольных битов: ", self.controlBits)
    def encode(self, line):
        stroka = [] # список, состоящий из элементов введённой строки
        a1 = 0 # счётчик для заполнения массива stroka
        n = 0
        for i in range(1, len(line) + self.controlBits + 1):
            if math.log(i, 2) != int(math.log(i, 2)): # вставка элементов введённой строки
                stroka.append(line[a1])
                a1 += 1
            else: # вычисление и вставка контрольных битов
                Bit = 0 # контрольный бит
                a2 = 0
                for j in range(1, len(line) + self.controlBits + 1):
                    if j != 0 and math.log(j, 2) != int(math.log(j, 2)):
                        Bit += int(line[a2]) if int(int(j / 2**n) & 1) == 1 else 0
                        a2 += 1
                stroka.append(Bit % 2)
                n += 1
        print("Закодированная строка двоичных символов: ", int(''.join(map(str, stroka))))
    def decode(self, line):
        stroka = [] # список, представляющий номер кода ошибки в двоичном виде
        n = 0
        i = 0 # счётчик
        while (2 ** i - 1) < len(line):
            sum = int(line[2 ** i - 1])
            a2 = 0
            for j in range(0, len(line)):
                if math.log(j + 1, 2) != int(math.log(j + 1, 2)):
                    sum += int(line[j]) if int(int((j+1) / 2**n) & 1) == 1 else 0
                    a2 += 1
            stroka.append(sum % 2)
            n += 1
            i += 1
        stroka.reverse()
        print("Код ошибки закодированной строки: ", int(''.join(map(str, stroka)), 2))
databits = int(input("Введите количество информационных разрядов: "))
kod = HammingEncoder(databits)
stroka = input("Введите строку двоичных символов: ")
kod.encode(stroka)
kod.decode("1011110")