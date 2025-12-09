import pytest
import allure
import requests

base_url = "https://restful-booker.herokuapp.com"
headers = { "Content-Type" : "application/json" }

@allure.title("TC01 - Create Token")
@allure.description("Verify that a token is created with valid username and password.")
@pytest.mark.smoke
def get_token(): #func 1
    path_post = "/auth"
    full_url = base_url + path_post
    json_payload = {
        "username" : "admin",
        "password" : "password123"
    }

    response_data = requests.post(url = full_url, headers= headers, json = json_payload)
    print(response_data)
    response_data_json = response_data.json()
    token = response_data_json["token"]
    assert  response_data.status_code == 200
    assert type(token) == str
    assert len(token) > 0
    return token

def get_bookingid(): #func 2
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
    print(response_data)

    response_data_json = response_data.json()
    bookingid = response_data_json["bookingid"]
    return bookingid

def test_put_reuest(): #func 3
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
        "firstname": "Damini",
        "lastname": "Sinha",
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
    # assert response.json()["firstname"] == "Pramod"
    assert response.json()["lastname"] == "Sinha"
    print(response.json()["firstname"])
    print(response.json()["lastname"])


def test_delete(): #func 4
    base_url = "https://restful-booker.herokuapp.com/booking/"
    booking_id = get_bookingid()
    DELETE_URL = base_url + str(booking_id)
    cookie = "token=" + get_token()
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }
    response = requests.delete(url=DELETE_URL, headers=headers)
    assert response.status_code == 201

#pytest -m "smoke" C:/Users/HP/PycharmProjects/PyATB5xLearning/Dec/ex_31122024_PyTest_requests_Module/test_Lab192_Pytest_Create_Token_POST.py --alluredir=allure_result2
#after this allure_result2 folder is created

#at last run the command , allure serve allure_result2
