# pytest main.py --alluredir=reports
# allure serve reports

import pytest
import allure
import requests

@allure.title("Verify the GET Request of Restful Booker")
@allure.description("This Testcase check Booking 1 and verify the response")
@pytest.mark.positive
def test_get_request_positive():
    url_get = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url=url_get)
    assert response_data.status_code == 200
    print("positive")

@allure.title("Verify the GET Request of Restful Booker with invalid ID")
@allure.description("This Testcase check Booking -1 and verify the response")
@pytest.mark.positive
def test_get_request_negative():
    url_get = "https://restful-booker.herokuapp.com/booking/-1"
    response_data = requests.get(url=url_get)
    assert response_data.status_code == 404
    print("negative")

# method 2
@allure.title("Verify the GET Request of Restful Booker")
@allure.description("This Testcase check Booking 1 and verify the response")
@pytest.mark.positive
def test_get_request_positive():
    assert requests.get(url="https://restful-booker.herokuapp.com/booking/1").status_code == 200
    print("positive")

@allure.title("Verify the GET Request of Restful Booker with invalid ID")
@allure.description("This Testcase check Booking -1 and verify the response")
@pytest.mark.positive
def test_get_request_negative():
    assert requests.get(url="https://restful-booker.herokuapp.com/booking/-1").status_code == 404
    print("negative")
