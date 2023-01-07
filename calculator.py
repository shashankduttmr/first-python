def Calculator():
    operations = ['-', '+', "*", "/"]
    for i in range(len(operations)):
        print(f'{i} for {operations[i]}')

    try:
        inp = int(input('enter your Choice:\n'))
        if (inp > len(operations)):
            print('invalid input Enter valid value')
        else:
            def Add(n1, n2):
                return n1+n2

            def Subtract(n1, n2):
                return n1-n2

            def Multiple(n1, n2):
                return n1*n2

            def Division(n1, n2):
                return n1/n2
            print(f'Your Choice is {operations[inp]}')
            n1 = float(input('Enter first value:\n'))
            n2 = float(input('Enter second value:\n'))
            if (operations[inp] == '-'):
                result = Subtract(n1, n2)
                print(f'{n1} - {n2} = {result}')
            elif(operations[inp] == '+'):
                result = Add(n1, n2)
                print(f'{n1} + {n2} = {result}')
            elif(operations[inp] == '*'):
                result = Multiple(n1, n2)
                print(f'{n1} * {n2} = {result}')
            elif(operations[inp] == '/'):
                result = Division(n1, n2)
                print(f'{n1} / {n2} = {result}')

    except:
        print('Please enter valid Input')


Calculator()
