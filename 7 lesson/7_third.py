#через return
a=int(input('Введите чему равна сторона квадрата: '))
def sq(a):
    p=4*a
    s=a*a
    return p,s
    
print(sq(a))

#print
a=int(input('Введите чему равна сторона квадрата: '))
def sq(a):
     print('Периметр квадрата =',4*a)
     print('Площадь квадрата =',a*a)

sq(a)

