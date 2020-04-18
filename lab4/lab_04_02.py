class Worker:
    'doc class Worker'
    count = 0
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        Worker.count += 1
    def display(self):
        print("Worker:")
        print("{} {}".format(self.name,self.surname))
w1 = Worker("Ivan", "Ivanov")
print("w1.count: ", w1.count)
w2 = Worker("Alexei", "Petrov")
print("w2.count: ", w2.count)
print("w1.count: ", w1.count)
print("Worker.count: {0} \n".format(Worker.count))
print("Worker.__name__: ", Worker.__name__)
print("Worker.__dict__: ", Worker.__dict__)
print("Worker.__doc__: ", Worker.__doc__)
print("Worker.__bases__: ", Worker.__bases__)
'''
Дополнение кода программы
'''
class Animal:
    count = 1
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.count = Animal.count
        Animal.count += 1
    def display(self):
        print("Animal {} : ".format(self.count))
        print(" Name: ", self.name)
        print(" Age: ", self.age)
a1 = Animal("Cat", 2)
a2 = Animal("Dog", 4)
a3 = Animal("Parrot", 1)
print("\n")
a1.display()
print("\n")
a2.display()
print("\n")
a3.display()

