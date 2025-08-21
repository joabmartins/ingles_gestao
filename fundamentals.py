msg = "Hello"
user = "Ysa"
# como definir uma função
def greeting(msg, user):
    '''
    function to say hi to the user
    msg: message to be printed
    user: user's name
    '''
    # concatenation - concatenação
    print(msg + ', ' + user + '!')
    # f-string
    print(f'Welcome, {user}!')
    # repeating
    print('Hi!'*3)
greeting(msg, user)

def basic_op(a, b):
    # Addition - Adição
    sum_result = a + b
    # Subtraction - Subtração
    difference_result = a - b
    # Multiplication - Multiplicação
    product_result = a * b
    # Division - Divisão
    division_result = a / b
    print(f'a + b = {sum_result}')
    print(f'a - b = {difference_result}')
    print(f'a * b = {product_result}')
    print(f'a / b = {division_result}')
basic_op(5, 3)