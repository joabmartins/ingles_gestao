msg = "Hello"
user = "bianca" 


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
   # list function - funções basicas de listas
   #lengh - comprimento
   print(len(fruits_lists))
   #index - indice
   print(fruits_lists[2])
   #append(acrescentar), insert(inserir, delet(deletar/excluir)
   fruits_lists.append('melon')
   fruits_lists.insert(0, 'lemon')
   del fruits_lists[1]
   print(fruits_lists)
   #ordenar a lista: sorted 
   fruits_lists.sort
   print(fruits_lists)
   #valor minimo ou maximo - min max
   print(f' min: {min(fruits_lists)} - max {max(fruits_lists)}')

   list_num = [2, 5, 3, 9, 5]
   print(f'min: {min(list_num)} - max {max(list_num)}')
   # tuple - tupla é uma lista que nao pode ser modificada
   tuple = ('professor', 'aluno', 'diretor', 'cozinheira')
   print(tuple)
   
   # set- conjunto de itens não repitidos e nao ordenados 
   animals = set(['rabbit', 'dog', 'cat', 'dog'])
   print(animals)
   animals.add('lion')
   animals.remove('cat')
   print(animals)
   
collections( )


#controles de fluxo
def flow_control(num ):
   #conditional statement: se condição então verdade senão falso
   print('-'*30)
   # verificar se o numero recebido è par ou impar
   if num % 2 == 0:
       print(f'{num} is even.')#even =  par
   else:
       print(f'{num} is odd.')#odd = impar

    #verificar a sençação do clima: quente, adravel, frio
   print('-'*30)
   temperature = 25
   if temperature > 30: #se temp for maior q 30 
        print("it's hot outside!") # está quente
   elif temperature > 20: #senão, se temp. maior q 20
        print("the weather is pleasant today!")#clima agradavel
   elif temperature > 10: #  senão, se temp. for maior q 10
        print("it's cold outside!") #está frio

   #apto para aposentadoria
   print('-'*30)
   idade= 59
   contribuicao = 20
   if idade > 65 and contribuicao > 15:
       print('apto para se aposentar')
   else:
       print('não apto para se aposentar')

   #for = para cada item da lista faça:
   print('-'*30)
   students= ['alace' , 'bob' , 'charlie' , 'diana']
   for name in students:
      print(name)
   else:
       print("nenhum aluno restante")

       #fazer algo ate que a condiçao seja falsa
       print('-'*30)
       counter=0
       while (counter <= 15):
           print(counter)
           # counter = counter +1
           counter = counter + 1
           counter += 1



flow_control(30)
