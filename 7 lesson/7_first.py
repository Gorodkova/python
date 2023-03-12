a=int(input('Введите первое число: '))
b=int(input('Введите второе число: '))
def sum(a,b):
    s=0
    if a<b:
        for i in range(a,b+1):
            s+=i
    else:
        for i in range(b,a+1):
            s+=i
    return s

print(sum(a,b))