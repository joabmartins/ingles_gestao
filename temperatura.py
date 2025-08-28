def flow_control(num):
    print('_'*30)
    if num % 2==0:
        print(f"(num) is even. ")
    else:
        print(f"(num) is odd. ")


    print('_'*30)


    temperature = 25
    if temperature > 30:
        print("It's hot outside!")
    elif temperature > 20:
        print("The weather is pleasant today!")
    elif temperature > 10:
        print("It's cold outside!")

    print('_'*30)
    idade = 50
    contribuicao = 20
    if idade > 65 and contribuicao > 15:
        print('apto para se aposentar!')
    else:
        print('nao apto para se aposentar! ')

    students = ['alece', 'bob', 'charle', 'diana']
    for name in students:
        print(name)
    else:
        print("memhum aluno restante")
    counter = 0 
    while (counter <= 15):
        print(counter)
    counter += 1


    flow_control(6)
