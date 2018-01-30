from nose.tools import *
from bin.app import app
from tests.tools import assert_response

def test_index():
    # check that we get a 404 on the / URL
    resp = app.request("/")
    assert_response(resp, status="404")

    # test our first GET request to /hello
    resp = app.request("/game")
    assert_response(resp)

    # make sure default values work for the form
    resp = app.request("/game", method="POST")
    assert_response(resp, contains=None)

    # test that we get expected values
    data = {'action': 'north'}
    resp = app.request("/game", method="POST", data=data)
    assert_response(resp, contains="north")
