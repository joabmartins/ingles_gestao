# /FANdaMENtols/

# Function /FANkxan/ and variable /VEriabol/
msg = 'Hello World!' # variável
def greeting(param_msg): # definição da função. param_msg: parâmetro
     print(param_msg) # ação a ser realizada
greeting(msg) # chamada da função

# Docstring
msg = 'Hello'
user = 'Joab'
def geeting2(msg, user):
     '''
     function to say hi to the user
     msg: message to be printed
     user: user's name
     '''
     print(msg)
     print(user)

     # --- após ensinar concatenação e f-string

     # concatenation
     print(msg + ' ' + user + '!')

     # f-string
     print(f'Welcome {user}!')

     # repeating
     print('Hi!'*3)

geeting2(msg, user)

# Concatenation f-string
# concatenar vários caracteres para formar um separador
def basic_op(a, b):

     # concat para criar um separador:
     print('-'*30)

     # Addition
     sum_result = a + b # 8

     # Subtraction
     difference_result = a - b # 2

     # Multiplication
     product_result = a * b # 15

     # Integer Division
     division_result = a / b # 1.666...
     integer_division_result = a // b # 1 (ignora a parte decimal)
     modulo_result = a % b # 2 (resto, sobra)
     print(f'[a + b = {sum_result}] [a - b = {difference_result}] [a * b = {product_result}] ')
     print(f'[a / b = {division_result}] [a // b = {integer_division_result}] [a % b = {modulo_result}] ')
    
basic_op(5, 3)
basic_op(3.14, -0.001)

# collections - coleções de valores
def collections():
     print('-'*30)
     # list - coleção de objetos ordenada (ordered) - or:ded
     fruit_list = ['apple', 'banana', 'orange', 'grape']

     # list functions - funções básicas de listas
     # length - comprimento
     print(len(fruit_list))
     # index - indice (listas tem uma ordem, imposta pelo índice, índice começa no zero, pode negativos para o contrário)
     print(fruit_list[2])
     # append and delete
     fruit_list.append('melon')
     fruit_list.insert(0, 'lemon')
     del fruit_list[1]
     print(fruit_list)
     # sort - classifica segundo algum critério (numérico, alfabético)
     fruit_list.sort()
     print(fruit_list)
     # min - max
     print(f'min: {min(fruit_list)} - max: {max(fruit_list)}')

     # tuple - tupla é uma lista que não pode ser modificada
     tuple = (1, 2, 3, 4)

     # set - conjunto é uma lista não ordenada (sem índices) e que não pode ter itens repetidos
     animals = set(['rabbit', 'dog', 'cat', 'dog'])
     print(animals)
     animals.add('lion')
     animals.remove('cat')
     print(animals)

collections()

def flow_control(num):
     # conditional statement
     print('-'*30)
     if num % 2 == 0:
          print(f'{num} is even.')
     else:
          print(f'{num} is odd.')
     
     # else if / elif
     print('-'*30)
     temperature = num * 5
     print(f'{temperature} °C')
     if temperature > 30:
          print("It's hot outside! Stay hydrated.") # haidreitid
     elif temperature > 20:
          print("The weather is pleasant today!")
     elif temperature > 10:
          print("It's cold outside! Dress warmly.")

     # nested if
     print('-'*30)
     genero = 'homem'
     contribuicao = 25
     if (genero == 'homem'):
          if (contribuicao > 15):
               print('pode se aposentar (nested if)')
     if genero == 'homem' and contribuicao > 15:
          print('pode se aposentar (and if)')

     # not in
     print('-'*30)
     random_numbers = [1, 2, 5, 7, 8, 0]
     if num not in random_numbers:
          print(f'{num} is not in the list!')
     else:
          print(f'{num} is in the list!')

     # for loop
     print('-'*30)
     students = ["Alice", "Bob", "Charlie", "Diana"]
     for name in students: # in range(3)
          print(f'Hello, {name}')
     # for loop and else
     else:
          print("no students left")
     
     # for loop using range
     print('-'*30)
     total_sum = 0
     for n in range(1, num):
          total_sum += n
     print(f'The sum of numbers from 1 to {num - 1} is {total_sum}')

     # while loop
     print('-'*30)
     counter = 0
     while counter < 5:
          counter += 1
          print(f'counting... total: {counter}')

     # continue
     # cria uma função que calcula a soma apenas dos números maiores do que o número informado
     print('-'*30)
     numbers = [1, 2, 3, 4, 5, 6]
     soma = 0
     for num in numbers:
          if num <= n:
               continue
          else:
               soma = soma + num
               print(f'number {num}, total: {soma}')
     
     # break
     print('-'*30)
     for num in numbers:
          if num == n:
               print(f'encontrou o número: {n}.')
               break
          print(f'ainda não encontrou o número {n}.  atual: {num}')

     # continue and break
     counter = 0
     while counter < 10:
          counter += 1
          if counter == 3:
               continue
          elif counter == 8:
               break
          print(f'current number: {counter}')

# passe um número até 10
flow_control(4)