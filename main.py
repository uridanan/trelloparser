# Python program to read
# json file


import json

# Opening JSON file
f = open('0TAdcIE5.json')

# returns JSON object as 
# a dictionary
data = json.load(f)

# Iterating through the json
# list
cards = data['cards']
checklists = data['checklists']

cardsDict={}
for c in cards:
    id = c['id']
    name = c['name']
    archived = c['closed']
    cardsDict[id] = {'name': name, 'archived': archived}

for i in checklists:
    cardId = i['idCard']
    name = i['name']
    items = i['checkItems']
    cardName = cardsDict[cardId]['name']
    archived = cardsDict[cardId]['archived']
    if not archived:
        print('----------------------------------------------------------------------')
        print(cardName)
        print(name)
        for item in items:
            print('-' + item['name'])
        print('\n')



# Closing file
f.close()