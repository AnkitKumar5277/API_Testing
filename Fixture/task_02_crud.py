# 2. Create a Booking, Delete the Booking with ID and Verify using GET request that it should not exist.

import pytest
import allure
import requests

base_url = "https://restful-booker.herokuapp.com"
headers = { "Content-Type" : "application/json" }

@allure.title("TC02 - Create, Delete and Verify")
@allure.description("Verify that a token&booking id is created and then verify the get response after deletion.")
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
    print(token)
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
    print("The Booking Id " + str(bookingid) + " is created.")
    return bookingid

def test_delete():
    base_url = "https://restful-booker.herokuapp.com/booking/"
    booking_id_del = get_bookingid()
    DELETE_URL = base_url + str(booking_id_del)
    cookie = "token=" + get_token()
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }
    response = requests.delete(url=DELETE_URL, headers=headers)
    assert response.status_code == 201
    # assert response.status_code == 200
    print("The Booking Id " + str(booking_id_del) + " is deleted.")
    return booking_id_del

def test_get_request():
    base_url = "https://restful-booker.herokuapp.com/booking/"
    booking_id_get = test_delete()
    GET_URL = base_url + str(booking_id_get)
    response_data = requests.get(url = GET_URL)
    assert response_data.status_code != 200
    assert response_data.status_code == 404
    assert response_data.text == "Not Found"
    print("We are getting status code - 404 as " + str(booking_id_get) + " is now deleted.")
    
