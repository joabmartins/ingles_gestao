msg = "Hello"
user = "Joseph"
   # como definir uma função
def greeting(msg, user):
    '''
    function to say hi to the User
    msg: message to be printed
    user: user's name
    '''
    # concatenation - concatenaçao
    print(msg + ', ' + user + '!')
    # f-string
    print(f'welcome, {user}!')
    # repeating
    print('hi!'*3)
greeting(msg, user)

def basic_op(a, b):
    # Addition - adição
    sum_result = a + b
    # subtraction - subtração
    difference_result = a - b
    # multiplication - multiplicação
    product_result = a * b
    # Division - divisão
    division_result = a / b
    print(f'a + b = {sum_result}')
    print(f'a - b = {difference_result}')
    print(f'a * b = {product_result}')
    print(f'a / b = {division_result}')
    # obter o resto da divisão
    modulo_result = a % b 
    print(f'a % b = {modulo_result}')

basic_op(5, 3)    



# collections - coleções de valores
def collections():
    print('-'*30)
    # list - coleção de objetos ordnada (ordered)
    fruits_list = ['apple', 'banana', 'orange', 'grape']
    print(fruits_list)
    # list function - funções básicas de listas
    # length - comprimento
    print(len(fruits_list))
    # index - índece 
    print(fruits_list[-4])
    # append, (acrescentar),  insert, (inserir), delete (deletar/excluir) 
    fruits_list.append('melon')
    fruits_list.insert(0, 'lemon')
    del fruits_list[1]
    print(fruits_list)
    # ordenar a lista: sorted
    fruits_list.sort()
    print(fruits_list)
    # valor minimo ou valor máximo - min max
    print(f'min: {min(fruits_list)} - max {max(fruits_list)}')

    list_num = [2, 5, 3, 9, 5]
    print(f'min: {min(list_num)} - max {max(list_num)}')

    # tuple - tupla é uma lista que nao pode ser modificada
    tuple = ('professor', 'aluno', 'diretor', 'cozinheira')
    print(tuple)

    # set - conjunto 
    animals = set(['rabbit', 'dog', 'cat', 'dog'])
    print(animals)
    animals.add('lion')
    animals.remove('cat')
    print(animals)
    

collections()

# controle de fluxo
def flow_control(num):
    # conditional statement: se condição então verdade senão falso
    print('-'*30)
    # verificar se o número recebido é par ou ímpar
    if num % 2 == 0:
        print(f'{num} is even.') # even = par
    else:
        print(f'{num} is odd.')  # odd = ímpar

# verificar a sensação do clima: quente, agradável, frio
    print('-'*30)
    temperature = 25
    if temperature > 30: # se temp. maior que 30
        print("it's hot outside!") # está quente
    elif temperature > 20: # senão, se temp. maior que 20
        print("The weather is pleasant today!") # está agradável 
    elif temperature > 10: # senão, se temp. maior que 10
        print( "it's cold outside!") # está frio    


     # apto para aposentadoria
    print('-'*30)
    idade = 59
    contribuição = 20
    if idade > 65 and contribuição > 15:
        print('apto para se aposentar!')
    else: 
        print('não apto para se aposentar!')

        # for = para cada item da lista faça:
        students = ['Alice', 'bob', 'charlie', 'Diana']
    for name in students:
        print(name)    
    else: 
        print("nenhum aluno restante")

    # fazer algo ate que a condição seja falsa
    counter = 0
    while (counter <= 15):
        print(counter)
      #  counter = counter + 1
        counter += 1


        

           



flow_control(11)





    


