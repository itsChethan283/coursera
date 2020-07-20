def triple(value):
    return 3*value 

def triplestuff(a_list):
    new_list = map(triple, a_list)
    return new_list

things = [1, 2, 3]
print(things)
thing1 = triplestuff(things)
print(thing1)    


abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]

def abb(word):
    return word.upper()

def words(li):
    abbre = map(abb, )            #map(function, word)
    return abbre

def words(li):
    abbre = map(lambda word: word.upper(), li)
    return abbre


upper = words(abbrevs)
print(upper)