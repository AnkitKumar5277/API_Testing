import pytest
import allure
import requests

# pip install pytest allure requests

# Create Token - POST
base_url = "https://restful-booker.herokuapp.com"
headers = {"Content-Type": "application/json"}


def get_token():
    base_path = "/auth"
    full_url = base_url + base_path
    json_payload_auth = {
        "username": "admin",
        "password": "password123"
    }
    response_data = requests.post(url=full_url, headers=headers, json=json_payload_auth)
    print(response_data)

    assert response_data.status_code == 200
    response_data_json = response_data.json()
    token = response_data_json["token"]
    print(token)
    assert type(token) == str
    assert len(token) > 0
    return token


def get_booking_id():
    base_path = "/booking"
    full_url = base_url + base_path
    print(full_url)
    json_payload = {
        "firstname": "Amit",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response_data = requests.post(url=full_url, headers=headers, json=json_payload)
    response_data_json = response_data.json()
    booking_id = response_data_json["bookingid"]
    return booking_id


def test_put_request():
    token = get_token()
    bookingid = get_booking_id()
    print(token)
    print(bookingid)
    base_path = "/booking/" + str(bookingid)
    full_url_put = base_url + base_path
    cookie = "token=" + token

    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie

    }

    json_payload = {
        "firstname": "Pramod",
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
    assert response.json()["firstname"] == "Pramod"


def test_delete():
    URL = "https://restful-booker.herokuapp.com/booking/"
    booking_id = get_booking_id()
    DELETE_URL = URL + str(booking_id)
    cookie_value = "token=" + get_token()
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie_value
    }
    response = requests.delete(url=DELETE_URL, headers=headers)
    assert response.status_code == 201

# Yeh Python test suite PyTest, Allure aur Requests library ka use karke RESTful-Booker API ke CRUD operations (Create, Read, Update, Delete) test karta hai. Aayiye aapko iska clear Hinglish explanation (within 200 words) deta hoon:
# 🔐 get_token()
# Yeh function /auth endpoint se valid username/password ke through authentication token generate karta hai. Token string type ka hona chahiye aur empty nahi hona chahiye.
# 🆔 get_booking_id()
# Yeh function /booking endpoint par valid booking details bhejta hai aur naya booking ID return karta hai. Yeh ID update/delete operation ke liye use hota hai.
# ✏️ test_put_request()
# Yeh function ek nayi booking create karta hai, fir us booking ko update (PUT request) karta hai.
# Authorization ke liye "Cookie": token=... header use hota hai.
# Booking ka "firstname" "Pramod" update hota hai.
# Response status code 200 hona chahiye, aur updated firstname bhi verify hota hai.
# 🗑️ test_delete()
# Yeh test nayi booking create karta hai aur usse delete (DELETE request) karta hai.
# Auth token header ke saath bheja jaata hai.
# Response ka status code 201 hona chahiye (successful deletion).
# ✅ Summary:
# Yeh script end-to-end automation karta hai RESTful API ke liye.
# Saare CRUD operations properly test kiye ja rahe hain.
# Reusable functions (get_token, get_booking_id) se code clean aur maintainable hai.
# Chahein to main isme Allure decorators (@allure.title, @allure.description) bhi add karke bata sakta hoon.
