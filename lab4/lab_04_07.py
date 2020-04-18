class Row:
    id = 1 # идентификатор строки
    def __init__(self, collection, value):
        self.id = Row.id
        Row.id += 1
        self.collection = collection # список значений переменных для текущего значения функции
        self.value = value # значение функции
    def display(self): # вывод таблицы на экран
        line = ""
        for i in self.collection:
            line += str(i) + "   "
        return str(self.id) + "  " + line + "|     " + str(self.value)

class Table:
    def __init__(self, rowsNum):
        self.rowsNum = rowsNum # количество строк таблицы
        self.rows = list() # список объектов класса Row
    def addRow(self, row): #  добавление строки (объект row класса Row) в список
        for i in self.rows:
            if i.id == row.id:
                print("Ошибка: в списке уже находится строка с таким же идентифиатором!")
                break
        self.rows.append(row)
    def setRow(self, row): #  изменение строки (объект row класса Row)
        for i in range(0, len(self.rows)):
            if self.rows[i].id == row.id:
                self.rows[i] = row
                return
            else:
                print("Ошибка: в списке нет строки с таким же идентифиатором!")
    def getRow(self, rowId): # получение строки c идентификатором
        for i in range(0, len(self.rows)):
            if self.rows[i].id == rowId:
                return self.rows[i]
    def display(self): # вывод таблицы на экран
        line = "id x1  x2  x3   f(x1,x2,x3)\n"
        for i in range(0, len(self.rows)):
            line += str(self.rows[i].display()) + "\n"
        return line

class LogicFunction:
    def __init__(self, variablesNum, table):
        self.variablesNum = variablesNum #  количество переменных функции
        self.table = table # таблица истинности логической функции
    def getExpression(self): # вычислние и возвращение минимальной формулы логической функции.
        def minimal(mass):
            counter = [0] * (len(mass) - 1) # список, состоящий из количества различий между значениями переменных, при которых значение функции равно единице
            mass_index = [0] * (len(mass[0])) # список, состоящий из индексов переменных, значения которых в таблице истинности отличаются одной 1 или одним 0
            for i in range(0, len(mass) - 1): # сравнение строк таблицы истинности, значение функции в которых равно 1
                for j in range(len(mass[i])):
                    if mass[i][j] != mass[i + 1][j]:
                        counter[i] += 1
                        mass_index[i] = j
            for i in range(len(counter)): # удаление строки, отличающейся от других строк на одно значение
                if counter[i] == 1:
                    del mass[i]
            for i in range(len(mass_index) - 1):
                if mass_index[i] == 0:
                    mass_index.remove(mass_index[i])
            if len(mass) < len(counter):
                counter.remove(counter[1])
            for i in range(0, len(mass)): # '*' - обозначение элемента строки, который был отличен у двух строк
                for j in range(len(mass[i])):
                    if j == mass_index[i] and counter[i] == 1:
                         mass[i][j] = '*'
            return mass
        znach = list()
        for i in self.table.rows:  # создание списка значений переменных, при которых  значение функции равно единице
            if i.value == 1: znach.append(i.collection)
        print("Значения переменных, при которых  значение функции равно единице: ", znach)
        k = minimal(znach)
        counter_k = [0] * (len(k) - 1)
        for i in range(0, len(k) - 1, 2):
            for j in range(len(k[i])):
                if k[i][j] != k[i + 1][j]:
                    counter_k[i] += 1
        for i in range(len(counter_k)):
            if counter_k[i] == 1:
                znach = minimal(k)
        res = "" # минимальная формула
        j = -1
        for i in znach: # создание минимальной формулы
            if j != -1: res += "+"
            for j in range(0, len(i)):
                if i[j] != "*":
                    if i[j] == 1:
                        res += "x" + str(j + 1)
                    else:
                        res += '"x' + str(j + 1)
        return res
    def getTable(self):
        return self.table
    def printTable(self):
        print(str(self.table))
table = Table(8)
table.addRow(Row([0, 0, 0], 1))
table.addRow(Row([0, 0, 1], 1))
table.addRow(Row([0, 1, 0], 0))
table.addRow(Row([0, 1, 1], 0))
table.addRow(Row([1, 0, 0], 1))
table.addRow(Row([1, 0, 1], 1))
table.addRow(Row([1, 1, 0], 0))
table.addRow(Row([1, 1, 1], 0))
print(table.display())
l = LogicFunction(3, table)
print("Минимальная формула логической функции: ", l.getExpression())






