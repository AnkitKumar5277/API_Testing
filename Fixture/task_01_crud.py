# 1. Verify that Create Booking -> Put/Patch Request - Verify that firstName is updated.

import pytest
import allure
import requests

base_url = "https://restful-booker.herokuapp.com"
headers = { "Content-Type" : "application/json" }

@allure.title("TC01 - Create and Update Booking.1")
@allure.description("Verify that a token&booking id is created and then first name is updated")
def get_token():
    path_post = "/auth"
    full_url = base_url + path_post
    json_payload = {
        "username" : "admin",
        "password" : "password123"
    }
    response_data = requests.post(url = full_url, headers= headers, json = json_payload)
    response_data_json = response_data.json()
    token = response_data_json["token"]
    assert  response_data.status_code == 200
    return token

def get_bookingid():
    path_post = "/booking"
    full_url = base_url + path_post
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response_data = requests.post(url = full_url, headers = headers, json = payload)
    response_data_json = response_data.json()
    bookingid = response_data_json["bookingid"]
    return bookingid

def test_put_reuest():
    token = get_token()
    bookingid = get_bookingid()
    print(token)
    print(bookingid)
    base_path = "/booking/" + str(bookingid)
    full_url_put = base_url + base_path
    cookie = "token=" + token
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": cookie

    }
    json_payload = {
        "firstname": "Damini", #Updating First Name.
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.put(url=full_url_put, headers=headers, json=json_payload)
    assert response.status_code == 200
    assert response.json()["firstname"] == "Damini"
    print(response.json()["firstname"])

