msg = "Hello"
user = "Cristiana"
# Como definir uma função
def greeting(msg, user):
    '''
    Function to say hi to the user
    msg: messege to be printed
    user: user's nome
    '''
    # concatenation - concatenação
    print(msg + ', ' + user + '!')
    # f-string
    print(f'Welcome, {user}!')
    # repeating
    print('Hi!'*3)
greeting(msg, user)

def basic_op(a, b):
    # Addition - adição
    sum_result = a + b
    # Subtraction - subtração
    difference_result = a - b
    # Multiplication - multiplicação
    product_result = a * b
    # Division - divisão
    division_result = a / b

    print(f'a + b = {sum_result}')
    print(f'a - b = {difference_result}')
    print(f'a * b = {product_result}')
    print(f'a / b = {division_result}')
    # Ignorar parte decimal
    division_result = a // b
    print(f'a / b = {division_result}')
    # Obter o resto da divisão
    modulo_result = a % b
    print(f'a % b = {modulo_result}')
basic_op(5, 3)

# Colllections - Coleção de valores
def collections():
    print('_'*30)
    # List - coleção de objetos ordenada (ordered)
    fruits_list = ['apple', 'banana', 'orange', 'grape']
    print(fruits_list)
    # List function - funções básicas de listas
    # length - comprimento (tamanho)
    print(len(fruits_list))
    # index - índice
    print(fruits_list[1])
    # Quando coloca o sinal de (-) menos na frente do numero a lista imprime de trás para frente
    print(fruits_list[-1])
    # append (acrescentar), insert (inserir), delete (deletar ou excluir)
    fruits_list.append('melon')
    fruits_list.insert(0, 'lemon')
    del fruits_list[1]
    print(fruits_list)
    # Ordenar a lista: sorted
    fruits_list.sort()
    print(fruits_list)
    # Valor mínimo ou valor máximo - min / max
    print(f'min: {min(fruits_list)} - max {max(fruits_list)}')

    list_num = [2, 3, 5, 9, 5, 7]
    print(f'min: {min(list_num)} - max {max(list_num)}')
    
    # tuple - tupla é uma lista que não pode ser modificada
    tuple = ('professor', 'aluno', 'diretor', 'cozinheira')
    print(tuple)

    # set - conjunto de itens não repetidos e não ordenados (não repete os elementos)
    animals = set(['rabbit', 'dog', 'cat', 'dog', 'bird'])
    print(animals)
    animals.add('lion')
    animals.remove('cat')
    print(animals)


collections()
