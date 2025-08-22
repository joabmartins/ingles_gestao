msg = "Hello"
user = "Paula" 

# como definir uma função
def greeting(msg, user):
    '''
    function to say hi to the user
    msg: message to be prited
    user: user's name
    '''
    #concatenation-concatenação
    print(msg + ', ' + user + '!')
    #f-string
    print(f'welcome -*- {user}!')
    #repetating
    print('Hi!'*3)
greeting(msg, user)
def basic_op(a, b):
    # Addition - adição
    sum_result = a + b
    # Subtraction - subtração
    difference_result = a - b
    # Multiplication - multiplicaçõa
    product_result = a * b
    # Division - divisão
    division_result = a / b  
    print(f'a + b = {sum_result}')
    print(f'a - b = {difference_result}')
    print(f'a * b = {product_result}')
    print(f'a / b = {division_result}')  
#ignorar a parte decimal
    division_result + a // b
    print(f'a / b = {division_result}')
    modelo_result = a % b
    print(f' a % b = {modelo_result}')
basic_op(5, 3)

 #coleção de valores
def collections( ):
   print('-'*30)
   #list -  coleção de objetos ordenada
   fruits_lists= ['apple', 'banana', 'orange', 'grape']
   print(fruits_lists)
   #list funtion - funções básicas de listas 
   #length - comprimento
   print(len(fruits_lists))
   #index - índice
   print(fruits_lists[2])
   #append (acrescentar), insert(inserir), delete(deletar/excluir)
   fruits_lists.append('melon')
   fruits_lists.insert(0, 'lemon')
   del fruits_lists[1]
   print(fruits_lists)
   #ordenar a lista: sorted
   fruits_lists.sort()
   print(fruits_lists)
   #valor mínimo ou valor máximo - min max
   print(f'min: {min(fruits_lists)} - max {max(fruits_lists)}')

list_num = [2, 5, 3, 9, 5]
print(f'min: {min(list_num)} - max {max(list_num)}')

#tuple - tupla é uma lista que não pode ser modificada
tuple = ('professor', 'aluno', 'diretor', 'cozinheira')
print(tuple)

#set - conjunto de itens não repetidos e não ordenados
animals = set(['rabbit', 'dog', 'cat', 'dog'])
print(animals)
animals.add('lion')
animals.remove('cat')
print(animals)

collections( )