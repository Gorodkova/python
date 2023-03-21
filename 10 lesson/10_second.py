class Student:
    name = ' '
    number = 0
    age = 0

    def nam(self):
        print('Имя студента -', self.name)
    def num(self):
        print('Номер студента -', self.number)
    def ag(self):
        print('Возраст студента -', self.age)
    def changenum(self):
        a = int(input('Введите новый номер студента: '))
        self.number = a
        print('Номер студента изменен на ', self.number)
    def changeage(self):
        a = int(input('Введите верный возраст студента: '))
        self.age = a
        print('Возраст студнента изменен на ', self.age)

stud1 = Student()
stud1.name = 'Aleksey'
stud1.number = 3
stud1.age = 19

stud2 = Student()
stud2.name = 'Roman'
stud2.number = 2
stud2.age = 18

stud3 = Student()
stud3.name = 'Mariya'
stud3.number = 4
stud3.age = 20


stud3.ag()
stud2.changenum()



