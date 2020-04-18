class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    def display(self):
        print("Person: ")
        print(" First name: ", self.firstname)
        print(" Last name: ", self.lastname)
        print(" Age: ", self.age)
class Student(Person):
    count = 0
    def __init__(self, firstname, lastname, age, recordBook):
        Person.__init__(self, firstname, lastname, age)
        Student.count += 1
        self.studentID = Student.count
        self.recordBook = recordBook
    def display(self):
        print(" Status: Student")
        print(" Student ID: ", self.studentID)
        print(" RecordBook: ")
        print("  Mark 5: ", self.recordBook[0])
        print("  Mark 4: ", self.recordBook[1])
        print("  Mark 3: ", self.recordBook[2])
        print("  Mark 2: ", self.recordBook[3])
class Professor(Person):
    count = 0
    def __init__(self, firstname, lastname, age, degree):
        Person.__init__(self, firstname, lastname, age)
        Professor.count += 1
        self.professorID = Professor.count
        self.degree = degree
    def display(self):
        print(" Status: Professor")
        print(" Professor ID: ", self.professorID)
        print(" Degree: ", self.degree)
s1 = Person("Anastasia", "Posulikhina", 17)
s1.display()
s1 = Student("Anastasia", "Posulikhina", 17,[7, 4, 1, 0])
s1.display()
s2 = Person("Kate", "Dubova", 18)
s2.display()
s2 = Student("Kate", "Dubova", 18, [4, 4, 7, 3])
s2.display()
s3 = Person("Dmitry", "Deev", 18)
s3.display()
s3 = Student("Dmitry", "Deev", 18, [9, 5, 1, 0])
s3.display()

p1 = Person("Elizabeth", "Orlova", 31)
p1.display()
p1 = Professor("Elizabeth", "Orlova", 3, "Docent")
p1.display()
p2 = Person("Edward", "Kronov", 42)
p2.display()
p2 = Professor("Edward", "Kronov", 42, "Professor")
p2.display()
p3 = Person("Elena", "Dmitrieva", 28)
p3.display()
p3 = Professor("Elena", "Dmitrieva", 28, "Postgraduate")
p3.display()
