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

def get_all_activities():
    endpoint = "/activities"
    peticion = get(url + endpoint)
    return peticion

def get_activity(id):
    endpoint = "/activities/{}".format(str(id))
    peticion = get(url + endpoint)
    return peticion


def create_activity(id, activity_name, date, status):
    endpoint = "/activities"
    headers = {"Content-Type": "application/json"}
    payload = {
        "ID": id,
        "Title": "{}".format(activity_name),
        "DueDate": "{}".format(date),
        "Completed": status
    }
    peticion = post(url + endpoint, data=payload, headers=headers)
    return peticion


def edit_activity( id, activity_name, date, status):
    endpoint = "/activities/{}".format(str(id))
    headers = {"Content-Type": "application/json"}
    payload = {
        "ID": id,
        "Title": "{}".format(activity_name),
        "DueDate": "{}".format(date),
        "Completed": status
    }
    peticion = put(url + endpoint, data=payload, headers=headers)
    return peticion


def delete_activity(id):
    endpoint = "/activities/{}".format(str(id))
    peticion = delete(url + endpoint)
    return peticion
