import json, os
        
def setUser(a):
#firstname, lastname, discord
    with open(os.path.join('./json', 'people.json')) as f:
        data = json.load(f)
    list = []
    for person in data['people']:
        list.append(person[a])
    return list
    
def getBotId():
    with open(os.path.join('./json', 'bot_tokens.json')) as f:
        data = json.load(f)
    list = []
    for bot in data['bots']:
        list.append(bot['token'])
    return list