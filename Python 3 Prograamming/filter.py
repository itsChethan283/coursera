def fils(a_list):
    new = filter(lambda num: num % 2 == 0, a_list)
    return new
    
li = [1, 2, 3, 4, 5, 6]
print(fils(li))
