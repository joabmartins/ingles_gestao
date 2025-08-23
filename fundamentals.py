msg = "Hello"
user = "Gui"
#como definir uma função
def greeting(msg, user):
    '''
    function to say hi to the user
    msg: messege to be printed
    user: user's name
    '''
    # concatenation - concatenação
    print(msg + ', ' + user + '!')
    #f=string
    print(f'welcome, {user}!')
    # repeating
    print('hi!'*3)
greeting(msg, user)

def basic_op(a, b):
    # Addition - adição
    sum_result = a + b
    # Subtration - subtração
    difference_result = a - b
    # Multiplication - multiplicação
    product_result = a * b 
    # Division - divisão
    division_result = a / b 
    print(f'a + b = {sum_result}')
    print(f'a - b = {difference_result}')
    print(f'a * b {product_result}')
    print(f'a / b {division_result}')
    #ignorar parte decimal
    division_result = a // b 
    print(f'a / b {division_result}')
    #obter o resto da divisão
    modulo_result = a % b 
    print(f'a % b = {modulo_result}')
basic_op(5, 3)
#Colletions - coleções de valores
def colletions():
    print('-'*30)
    #list - coleção de objetos ordnada (ordaned)
    fruits_list = ['apple', 'banana', 'orange', 'grape']
    print(fruits_list)
    #list function - funções básicas de lsitas
    #lenght - comprimento
    print(len(fruits_list))
    #indsx - índice
    print(fruits_list[-4])
    # append (acrescentar), insert(inserir), delete(deleetar/excluir)
    fruits_list.append('melon')
    fruits_list.insert(0, 'lemon')
    del fruits_list[1]
    print(fruits_list)
    # ordenar a lista (sorted)
    fruits_list.sort()
    print(fruits_list)
    # valor minimo ou valor máximo - (min, max)
    print(f'min: {min(fruits_list)} - max: {max(fruits_list)}')

    list_num = [2, 5, 3, 9, 5]
    print(f'min: {min(fruits_list)} - max: {max(fruits_list)}')

    #tuple - tupla é uma lista que não pode ser modficadas
    tuple = ('professor', 'aluno', 'diretor', 'cozinheira')
    print(tuple)
    #set - conjunto de itens não repetidos e não ordenados
    animals = set(['rabbit', 'dog', 'cat', 'dog'])
    print(animals) 
    animals.add('lion')
    animals.remove('cat')
    print(animals)
colletions()


    #controles de fluxo
def flow_control(num):
    # connditional statement: se condição então veradade senão falso
    print('-'*30)
    # verificar se o número recebido é par ou ímpar
    if num % 2 == 0:
        print(f'{num} is even.') #even = par
    else:
        print(f'{num} is odd.') # odd = ímpar


    # verifcar a sensação do clima:  quente, agradável, frio
    print('-'*30)
    tempetature = 15
    if tempetature >30:  # se temperatura maior que 30
        print("It's hot outside!")
    elif tempetature >20: # senão, se temp. maior que 20  
        print("The weather is pleasent today!") # está agradável
    elif tempetature > 10:  # senão, temp. maior que 10
        print("It's cold outside!")  # está frio


    # apto para aposentadoria
    print('-'*30)
    idade = 50
    contribuicao = 20
    if idade > 65 and contribuicao > 15:
        print('apto para se aposentar!')
    else:
        print('não apto para se aposentar!')

    print("---------------------------")

    # for = para cad item de uma lista
    students = ['Alece', 'Bob', 'Charlie', 'Diana']
    for name in students:
        print(name)
    else:
        print('nenhum aluno restante!')
    
    print('-----------------------------')

    # fazer algo ate que a condição seja falsa 
    counter = 0
    while (counter <= 15):
        print(counter)
        # counter = counter + 1 
        counter = counter + 1


flow_control(6)            