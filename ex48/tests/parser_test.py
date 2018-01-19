from nose.tools import *
from ex48 import parser, lexicon

def test_peek():

    word_list1 = lexicon.scan("open the door")
    result = parser.peek(word_list1)
    assert_equal(result, 'verb')


def test_match():

    word_list2 = lexicon.scan("in the west")
    result = parser.match(word_list2, 'stop')
    assert_equal(result, ('stop', 'in'))


def test_skip():

    word_list1 = lexicon.scan("open the door")
    result = parser.skip(word_list1, 'stop')
    assert_equal(result, None)


def test_parse_verb():

    word_list1 = lexicon.scan("open the door")
    result = parser.parse_verb(word_list1)
    assert_equal(result, ('verb', 'open'))
    assert_raises(parser.ParserError, parser.parse_verb, word_list1)


def test_parse_object():

    word_list2 = lexicon.scan("in the west")
    result = parser.parse_object(word_list2)
    assert_equal(result, ('direction', 'west'))
    assert_raises(parser.ParserError, parser.parse_object, word_list2)


def test_parse_subject():

    word_list1 = lexicon.scan("open the door")
    result = parser.parse_subject(word_list1, ('noun', 'princess'))
    wanted = parser.Sentence(('noun', 'princess'), ('verb', 'open'), ('noun', 'door'))
    assert_equal(result.subject, wanted.subject)
    assert_equal(result.verb, wanted.verb)
    assert_equal(result.object, wanted.object)


def test_parse_sentence():

    word_list3 = lexicon.scan("princess open the door")
    result = parser.parse_sentence(word_list3)
    wanted = parser.Sentence(('noun', 'princess'), ('verb', 'open'), ('noun', 'door'))
    assert_equal(result.subject, wanted.subject)
    assert_equal(result.verb, wanted.verb)
    assert_equal(result.object, wanted.object)
    assert_raises(parser.ParserError, parser.parse_sentence, word_list3)
