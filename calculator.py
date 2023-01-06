def Calculator():
    operations = ['-', '+', "*", "/" ,"//"]
    for i in range(len(operations)):
        print(f'{i} for {operations[i]}')

    try:
        inp = int(input('enter your Choice:\n'))
        if(inp > len(operations)):
            print('invalid input Enter valid value')
    except:
        print('Please enter valid Input')   


Calculator()