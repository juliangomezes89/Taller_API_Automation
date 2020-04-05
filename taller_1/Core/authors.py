import sys
sys.path.extend(['C:/Users/julia/PycharmProjects/Taller1/Taller_API_Automation/'])
from requests import post, get, delete, put

url = "https://fakerestapi.azurewebsites.net"

def set_url(_url):
    global url
    url = _url

def get_url():
    return  url

def get_author_by_book(id):
    endpoint = "/authors/books/{}".format(str(id))
    peticion = get(url + endpoint)
    return peticion

def get_all_authors():
    endpoint = "/api/Authors"
    peticion = get(url + endpoint)
    return peticion

def create_authors(id, id_book, firstname, lastname):
    endpoint = "/api/Authors/"
    headers = {"Content-Type": "application/json"}
    payload = {
        "ID": id,
        "IDBook": id_book,
        "FirstName":  "{}".format(firstname),
        "LastName":  "{}".format(lastname)
    }
    peticion = post(url + endpoint, data=payload, headers=headers)
    return peticion

def delete_authors(id):
    endpoint = "/api/Authors/{}".format(str(id))
    peticion = delete(url + endpoint)
    return peticion

def get_author(id):
    endpoint = "/api/Authors/{}".format(str(id))
    peticion = get(url + endpoint)
    return peticion

def edit_authors(id, id_book, firstname, lastname):
    endpoint = "/api/Authors/{}".format(str(id))
    headers = {"Content-Type": "application/json"}
    payload = {
        "ID": id,
        "IDBook": id_book,
        "FirstName": "{}".format(firstname),
        "LastName": "{}".format(lastname)
    }
    peticion = put(url + endpoint, data=payload, headers=headers)
    return peticion


