import json

data = '''
{
"name" : "chuck" ,
"phone" : {
"type" : "intl" ,
"number" : "+1 734 303 4456"
},
"email" : {
"hide" : "yes"
}
}'''
info = json.loads(data)
print('Names : ', info["name"])
print('Hide : ', info["email"]["hide"])
