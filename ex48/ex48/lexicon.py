# _*_ coding:utf-8 _*_

directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
verbs = ['go', 'stop', 'kill', 'eat']
stops = ['the', 'in', 'of', 'from', 'at', 'it']
nouns = ['door', 'bear', 'princess', 'cabinet']

def convert_number(word):
    try:
        return int(word)
    except ValueError:
        return None


def scan(sentence):

    words = sentence.split()
    result = []

    for word in words:
        if word in directions:
            result.append(('direction', word))
        elif word in verbs:
            result.append(('verb', word))
        elif word in stops:
             result.append(('stop', word))
        elif word in nouns:
            result.append(('noun', word))
        elif convert_number(word) <> None:
            result.append(('number', convert_number(word)))
        else:
            result.append(('error', word))

    return result
