list1=[3,7,9,10,62,77]
list2=[2,11,62,36,9,34]
def comp(list1,list2):
    for i in list1:
        for j in list2:
            if i==j:
                print('TRUE')
                break
            
comp(list1,list2)