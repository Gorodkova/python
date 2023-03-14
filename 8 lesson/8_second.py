numbers=[2,5,8,45,5,17,26,17,81,2,11,36,45,7]
newlist=[]
def delet(numbers):
    for i in numbers:
        if i not in newlist:
            newlist.append(i)
    print(newlist)

delet(numbers)


