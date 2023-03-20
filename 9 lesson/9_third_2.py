with open('3.txt', 'r') as file1:
    content = file1.read()

    numbers = ''

    for i in content:
        if i.isdigit():
            numbers +=i

    if numbers:
        with open('4.txt', 'w') as file2:
            file2.write(numbers)