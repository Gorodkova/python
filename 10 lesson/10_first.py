class Calc:
    a = 0
    b = 0

    def mult(self):
        print('Произведение = ', self.a * self.b)
    def sum(self):
        print('Сложение = ', self.a + self.b)
    def sub(self):
        print('Разность = ', self.a - self.b)
    def div(self):
        print('Частное = ', self.a / self.b)

res = Calc()
res.a = 56
res.b = 4
res.mult()
res.sum()
res.sub()
res.div()