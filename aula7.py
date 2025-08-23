#controle de fluxo
def flow_control(num):
    #se a condição verdade senão falso
    print('_'*30)
    #verificar se o número recebido é par ou impar    
    if num % 2==0:
        print(f"{num} is even. ")# par
    else: 
        print(f"{num} is odd. ")# impar
        
        
    print('_'*30)
    
    
    temperature = 25
    if temperature > 30:
        print("it's hot outside! ") #quente
        
    elif temperature > 20:
        print("the weather is pleasant today! ")# agradavel
        
    elif temperature > 10:
        print("it's cold outside! ")# frio
        
    print('_'*30)
    idade = 59
    contribuicao = 20
    if idade > 65 and contribuicao > 15:
        print('apto para se aposentar!')
    else:
        print('nao apto para se aposentar! ')
        
    students =  ['alece', 'bob', 'charlie', 'diana']
    for name in students:
        print(name)
        
    else:
        print("nenhum aluno restante")
    counter = 0
    while (counter <= 15):
        print(counter)
        counter +=1
        
flow_control(6)



        