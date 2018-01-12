# _*_ coding:utf-8 _*_

class lexicon(object):

    def __init__(self):
        self.directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
        self.verbs = ['go', 'stop', 'kill', 'eat']
        self.stops = ['the', 'in', 'of', 'from', 'at', 'it']
        self.nouns = ['door', 'bear', 'princess', 'cabinet']

    def convert_number(self, word):
        try:
            return int(word)
        except ValueError:
            return None


    def scan(self, sentence):

        words = sentence.split()
        result = []

        for word in words:
            if word in self.directions:
                result.append(('direction', word))
            elif word in self.verbs:
                result.append(('verb', word))
            elif word in self.stops:
                result.append(('stop', word))
            elif word in self.nouns:
                result.append(('noun', word))
            elif self.convert_number(word) <> None:
                result.append(('number', self.convert_number(word)))
            else:
                result.append(('error', word))

        return result

lexicon = lexicon()
