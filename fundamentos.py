
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
basic_op(5, 8)