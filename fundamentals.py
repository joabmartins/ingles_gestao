msg = "Hello"
user = "erica"

#Como definir uma função
def greeting(msg, user):
    '''
    Function to say hi to the user
    msg: message to be printed
    user: user's name
    '''
    #concatenation - concatenação
    print(msg + ', ' + user + '!')
    #f-string
    print(f'Welcome, {user}!')
    #repeating
    print('Hi!'*3)
greeting(msg, user)

def basic_op(a, b):
    #Addition - adição
    sum_result = a + b
    #Subtraction - subtração
    difference_result = a - b
    #Multiplication - multiplicação
    product_result = a * b 
    #Division 
    division_result = a / b
    print(f'a + b = {sum_result}')
    print(f'a - b = {difference_result}')
    print(f'a * b = {product_result}')
    print(f'a / b = {division_result}')
    #ignorar parte decimal
    division_result = a // b
    print(f'a / b = {division_result}')
    #obter o resto da divisão
    modulo_result = a % b
    print(f'a % b = {modulo_result}')
basic_op(5, 3)

#collections - coleções de valores 
def collections():
    print('-'*30)
    #list - coleção de objetos ordenada (ordered)
    fruits_list = ['apple', 'banana', 'orange', 'grape']
    print(fruits_list)
    #list function - funções básicas de listas
    #length - comprimento
    print(len(fruits_list))
    #index - índice
    print(fruits_list[2])
    #append(acrescentar), insert(inserir), delete(deletar/excluir)
    fruits_list.append('melon')
    fruits_list.insert(0, 'lemon')
    del fruits_list[1]
    print(fruits_list)
    #ordenar a list: sorted
    fruits_list.sort()
    print(fruits_list)
    #valor mínimo ou valor máximo - min e max
    print(f'min: {min(fruits_list)} - max {max(fruits_list)}')

    list_num = [2, 5, 3, 9,5]
    print(f'min: {min(list_num)} - max {max(list_num)}')

    #tuple - tupla é uma lista que não pode ser modificado
    tuple = ('professor', 'aluno', 'diretor', 'cozinheira')
    print(tuple)
    #set - conjunto de itens não repetidos e não ordenados
    animals = set(['rabbit', 'dog', 'cat', 'dog'])
    print(animals)
    animals.add('lion')
    animals.remove('cat')
    print(animals)
   
collections()