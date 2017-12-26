# -*- coding:utf-8 -*-
from sys import exit

def is_started():
    print "有学习的意愿是一件好事。"
    print "Have you started learning python yet? Yes/No | Y/n "

    next = raw_input("> ")

    if next in ["Yes", "Y", "yes", "y", "YES"]:
        which_ex()
    elif next in ["Not", "N", "not", "n", "NOT"]:
        print "有学习的意愿固然是一件好事，但仅仅只有意愿是远远不够的，动起来。"
        print "This is the end!"
        exit(-1)
    else:
        print "Please give an clearly answer!"
        desire_research()

def which_ex():
    print "赞，很高兴你已经开始了学习的旅途。"
    print "Which exercise you're working on? just give the ordinal of the exercise"

    next = raw_input("> ")

    while not next.isdigit():
        print "别调皮，快快输入正确的习题号！"
        next = raw_input("> ")
    else:
        ordinal = int(next)

    if ordinal > 52:
        print "你确定你的输入是正确的？"
        print "别逗我..."
        exit(2)
    elif ordinal > 18:
        print "Great! Keep going on learning."
        exit(0)
    elif ordinal > 11:
        print "Good, speed up your progress."
        exit(0)
    else:
        print "学习是一个不断坚持的过程，不要再拖拉下去"
        print "You need to think about what to do next."
        exit(0)

def desire_research():
    print """
    Do you want to learn python? Yes/No | Y/n
    """

    next = raw_input("> ")

    if next in ["Yes", "Y", "yes", "y", "YES"]:
        is_started()
    elif next in ["Not", "N", "not", "n", "NOT"]:
        print "OK, the end!"
        exit(-1)
    else:
        "Please give an clearly answer!"
        start()

def start():
    print "Let's make a desire research!"
    desire_research()

start()
