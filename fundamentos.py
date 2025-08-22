
msg = "hi"
user = "Danilo"
def greeting(msg, user):
    '''
function to say hi the user
msg: message to be printed
    '''
    #concatenation - concatenação
    print(msg + ',' + user + '!')
    # f-strng
    print(f'welcome { user}')
    #repeating
    print("hi!" *3)
greeting(msg, user)
def basic_op(a, b):
   #adition
   sum_result = a + b
   #subctration
   difference_result = a - b
   #miltplication
   product_resultion = a * b
   #division
   divission_result = a / b
   print(f'a + b = {sum_result}')
   print(f'a - b = {difference_result}')
   print(f'a * b = {product_resultion}')
   print(f'a / b = {divission_result}')
   #ignorar parte decimal
   division_result = a // b
   print(f"a / b = {division_result}")
   modulo_result = a % b 
   print(f"a % b = {modulo_result}")
basic_op(5, 8)
#collections
def collections():
    print('-' *30)
#list- objetos ordnados
fruits_list = ['apple', 'banana', 'orange', 'grape']
print(fruits_list)
#list function
#lenght
print(len(fruits_list))
#index
print(fruits_list[2])
#append (adicionar, inserir e deletar)
fruits_list.append('melon')
fruits_list.insert(0, 'lemon')
del fruits_list[1]
print(fruits_list)
#ordenar lista
fruits_list.sort()
print(fruits_list)
#valor max ou min
print(f'min: {min(fruits_list)} - max {max(fruits_list)}')
list_num = [2, 5, 3, 9, 7]
print(f'min: {min(list_num)} - max {max(list_num)}')
#tuple tupla uma lista que n pode ser modificada
tuple = ('professor', 'aluno', 'diretor')
print(tuple)
#set- conjunto de itens nao repetidos e não ordenados 
animals = set(['rabbit', 'dog', 'cat', 'dog'])
print(animals)
animals.add('lion')
animals.remove('cat')
collections()

#controle de fluxo
def flow_control(num):
#conditional statement: se condição verdadeiro ou falso
    print('-' *30)
   #verficar se é impar ou par
    if num % 2 == 0:
       print(f'{num} is even.')
    else:
       print(f'{num} is odd.')
       #verificar a sensação do clima: hot, agradavel ou frio
    temp = 25
    if temp > 30:
        print("it's hot outside! ")
    elif temp > 20: #se não
        print("thte weather is pleasant today!")
    elif temp > 10:
        print("it's cold outside!")
#apto aposentaria
    idade = 66
    cont = 20
    if idade > 65 and cont > 15:
        print(" voce está apto a se aposentar")
    else:
        print("inapto a se aposentar!")
#for = para cada item da lista faça:
    students=['alice', 'bob', 'charlie', "diana"]
    for name in students:
        print(name)
flow_control(6)
