from builtins import map
List = {1, 2, 3, 4, 10, 123, 22}  
def sum(x):
    return x + x

y = map(lambda x:x + x, List)
for element in y:
    print(element)

