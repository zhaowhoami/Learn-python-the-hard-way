# -*- coding:utf-8 -*-

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

mother = ["世上只有妈妈好", "有妈的孩子像块宝", "投进妈妈的怀抱", "幸福享不了"]

Song(mother).sing_me_a_song()
