import sys
import time
from datetime import datetime, timedelta

sys.path.extend(['C:/Users/julia/PycharmProjects/Taller1/Taller_API_Automation/'])
from requests import post, get, delete, put

url = "https://fakerestapi.azurewebsites.net/api"

def set_url(_url):
    global url
    url = _url

def get_url():
    return  url

def get_all_books():
    endpoint = "/Books"
    peticion = get(url + endpoint)
    return peticion

def create_book(id, book_title, book_description, page_count, excerpt, date):
    endpoint = "/Books"
    headers = {"Content-Type": "application/json"}
    payload = {
        "ID": id,
        "Title": "{}".format(book_title),
        "Description": "{}".format(book_description),
        "PageCount": page_count,
        "Excerpt": "{}".format(excerpt),
        "PublishDate": "{}".format(date)
    }
    peticion = post(url + endpoint, data=payload, headers=headers)
    return peticion

def delete_book(id):
    endpoint = "/Books/{}".format(str(id))
    peticion = delete(url + endpoint)
    return peticion

def get_book(id):
    endpoint = "/Books/{}".format(str(id))
    peticion = get(url + endpoint)
    return peticion

def edit_book( id, book_title, book_description, page_count, excerpt, date):
    endpoint = "/Books/{}".format(str(id))
    headers = {"Content-Type": "application/json"}
    payload = {
        "ID": id,
        "Title": "{}".format(book_title),
        "Description": "{}".format(book_description),
        "PageCount": page_count,
        "Excerpt": "{}".format(excerpt),
        "PublishDate": "{}".format(date)
    }
    peticion = put(url + endpoint, data=payload, headers=headers)
    return peticion


