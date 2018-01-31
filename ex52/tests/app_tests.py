from nose.tools import *
from bin.app import app
from tests.tools import assert_response

def test_index():
    # check that we get a 303 on the / URL
    resp = app.request("/")
    assert_response(resp, status="303")

    # test our first GET request to /hello
    resp = app.request("/game")
    assert_response(resp)

    # make sure default values work for the form
    resp = app.request("/game", method="POST")
    assert_response(resp, status="303")

    # test that we get expected values
    data = {'action': 'tell a joke'}
    resp = app.request("/game", method="POST", data=data)
    assert_response(resp, status="303")
