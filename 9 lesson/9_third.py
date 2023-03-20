def findnum(file1, file2):
    with open(file1) as doc1:
        with open(file2, 'a') as doc2:
            read1 = doc1.read()
            for i in read1:
                if i != 0:
                    doc2.write(i)

findnum('3.txt', '4.txt')


