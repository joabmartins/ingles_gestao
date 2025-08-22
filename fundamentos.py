def basic_op(a, b):
    sum_result = a + b
    difference_result = a - b
    product_result = a * b
    division_result= a/ b
    print(f'a + b = {sum_result}')
    print(f"a - = {difference_result}")
    print(f"a * b = {product_result}")
    print(f"a / b = {division_result}")

basic_op(5, 3)

def collections():
    print('_'*60)
    fruits_list = ['apple', 'banana', 'orange', 'grape', 'pineple']
    print(fruits_list)
    print(fruits_list[2])
    
    fruits_list.append('melon')
    fruits_list.insert(0,   'lemon')
    del fruits_list[1]
    print(fruits_list)
    print(f'min: {min(fruits_list)} - max {max(fruits_list)}')
    
    
    
    
    
    animals = set('rabbit', 'dog', 'cat', 'dog')
    print(animals)
    animals.add('lion')
    animals.remove('cat')
    print(animals)
    
collections()