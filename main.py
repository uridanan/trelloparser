# Python program to read
# json file


import json


def checklists2description(filename):
    # Opening JSON file
    f = open(filename + '.json')

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Closing file
    f.close()

    # Iterating through the json
    # list
    cards = data['cards']
    checklists = data['checklists']
    descriptions = []

    cardsDict={}
    for c in cards:
        cardId = c['id']
        cardsDict[cardId] = c

    for i in checklists:
        cardId = i['idCard']
        name = i['name']
        items = i['checkItems']
        cardName = cardsDict[cardId]['name']
        archived = cardsDict[cardId]['closed']
        description = ''  # cardsDict[cardId]['desc']
        if not archived:
            description = description + '\n' \
                          + '----' + '\n' \
                          + '**' + name + '**' + '\n'
            for item in items:
                done = ''
                if item['state'] == 'complete':
                    done = ' - DONE'
                description = description + '-' + item['name'] + done + '\n'
            description = description + '\n'
        cardsDict[cardId]['desc'] += description
        descriptions.append(description)

    data['cards'] = cards

    # Writing to sample.json
    with open(filename + '-corrected.json', 'w') as outfile:
        outfile.write(json.dumps(data))


checklists2description('Board-URI')
