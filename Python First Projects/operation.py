def operation():
    numb1 = int(input("Insert first number = "))
    numb2 = int(input("Insert second number = "))
    operation = input("Insert operation type = ")
    plus = ['+','-','*', '/']
   
    if operation == plus[0]:
        result = numb1 + numb2
        print (f'The result: {numb1} + {numb2} = {result}')
    elif operation == plus[1]:
        result = numb1 - numb2
        print (f'The result: {numb1} - {numb2} = {result}')
    elif operation == plus[2]:
        result = numb1 * numb2
        print (f'The result: {numb1} * {numb2} = {result}')
    elif operation == plus[3]:
        result = numb1 / numb2
        print (f'The result: {numb1} / {numb2} = {result}')
operation()
     
