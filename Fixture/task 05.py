# 5. Invalid Creation - enter a wrong payload or Wrong JSON.

import requests

base_url = "https://restful-booker.herokuapp.com"
headers = {"Content-Type": "application/json"}


def test_invalid_creation():
    path_post = "/booking"
    full_url = base_url + path_post
    payload = {
        "*firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response_data = requests.post(url=full_url, headers=headers, json=payload)
    assert response_data.status_code == 500
    assert response_data.text == "Internal Server Error"
