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
basic_op(5, 3)    


    


