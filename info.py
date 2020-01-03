import json

class info:
    def __init__(self, firstname, lastname, discord):
        self.firstname  = firstname
        self.lastname   = lastname
        self.discord    = discord
                                       
    def fullname(self):
        return f"{self.firstname} {self.lastname}"
        
def setUser(a):
#firstname, lastname, discord
    with open('info.json') as f:
        data = json.load(f)
    list = []
    for person in data['people']:
        list.append(person[a])
    return list
    
def getBotId():
    with open('bot.json') as f:
        data = json.load(f)
    list = []
    for bot in data['bots']:
        list.append(bot['id'])
    return list