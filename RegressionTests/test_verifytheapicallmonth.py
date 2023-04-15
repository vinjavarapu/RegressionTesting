import requests
import pytest

url = "https://lx8ssktxx9.execute-api.eu-west-1.amazonaws.com/Prod/next-birthday?dateofbirth=1974-04-10&unit=month"
url_emptyarguments = "https://lx8ssktxx9.execute-api.eu-west-1.amazonaws.com/Prod/next-birthday?dateofbirth=&unit="
url_wronginput = "https://lx8ssktxx9.execute-api.eu-west-1.amazonaws.com/Prod/next-birthday?dateofbirth=19740410&unit=month"
url_onlyyearinput = "https://lx8ssktxx9.execute-api.eu-west-1.amazonaws.com/Prod/next-birthday?dateofbirth=1974-04-10"
url_onlyunitinput = "https://lx8ssktxx9.execute-api.eu-west-1.amazonaws.com/Prod/next-birthday?dateofbirth=&unit=month"

def test_can_call_apiendpoint():
    response = requests.request("GET", url)
    response_body = response.json()
    status_code = response.status_code
    assert status_code == 200
def test_verifymessagebody():
    response = requests.request("GET", url)
    response_body = response.json()
    message = response_body.get('message')
    print(message)
def test_verifyapiresponse_emptyarguments():
    response = requests.request("GET", url_emptyarguments)
    response_body = response.json()
    message = response_body.get("message")
    assert message == "Please specify both query parameter dateofbirth and unit"
def test_verifyapiresponse_wronginput():
    response = requests.request("GET", url_wronginput)
    response_body = response.json()
    message = response_body.get("message")
    assert message == "Please specify dateofbirth in ISO format YYYY-MM-DD"
def test_verifyapiresponse_onlyyearinput():
    response = requests.request("GET", url_onlyyearinput)
    status_code = response.status_code
    print(status_code)
    assert status_code == 400
    response_body = response.json()
    message = response_body.get("message")
    assert message == 'Please specify both query parameter dateofbirth and unit'

def test_verifyapiresponse_onlyunitinput():
    response = requests.request("GET", url_onlyunitinput)
    status_code = response.status_code
    print(status_code)
    assert status_code == 400
    response_body = response.json()
    message = response_body.get("message")
    assert message == 'Please specify both query parameter dateofbirth and unit'










