import pytest

@pytest.fixture()
def create_token():
    return "abc"

@pytest.fixture()
def create_booking_id():
    return 1

@pytest.fixture()
def read_excel_file():
    return "xyz"

def test_put(create_token, create_booking_id):
    print(create_token)
    print(create_booking_id)

def test_put_2(create_token, create_booking_id, read_excel_file):
    print(create_token)
    print(create_booking_id)
    print(read_excel_file)

# Is code mein **`pytest`** framework ka use kiya gaya hai jismein **fixtures** define kiye gaye hain. Fixtures test run se pehle kuch data ya setup provide karte hain.
# * `create_token()` fixture ek dummy token `"abc"` return karta hai.
# * `create_booking_id()` ek booking ID `1` return karta hai.
# * `read_excel_file()` ek file ka naam `"xyz"` return karta hai.
# Phir do test functions hain:
# 1. **`test_put()`**: ye `create_token` aur `create_booking_id` ko use karke unka print karta hai.
# 2. **`test_put_2()`**: ye teeno fixtures ko use karta hai aur unki values print karta hai.
# Fixtures automatically inject ho jaate hain test functions mein.

import pytest

@pytest.fixture()
def create_token():
    return "abc"

@pytest.fixture()
def create_booking_id():
    return 123

def test_update_req_1(create_token, create_booking_id):
    print("Token ->", create_token)
    print("Booking ID -> ", create_booking_id)

# Is code mein hum pytest ka use kar rahe hain testing ke liye. Yahaan fixture ek special function hota hai 
# jo test case chalne se pehle kuch data ya setup provide karta hai.
# 🔹 @pytest.fixture() decorator se create_token() aur create_booking_id() functions define kiye gaye hain.
# 🔹 create_token() function "abc" return karta hai aur create_booking_id() 123 return karta hai.
# 🔹 test_update_req_1() ek test function hai jo in dono fixtures ka use karta hai.
# 🔹 Test ke dauraan print() ke through token aur booking ID screen par show ki jati hai.
# Fixtures se reusable test data milta hai, aur code clean rehta hai.

import allure  # pip install allure
import pytest  # pip instal pytest
import requests  # pip install requests

# pytest main.py --alluredir=reports
# allure serve reports
import pytest

@pytest.fixture()
def create_token():
    return "abc"

@pytest.fixture()
def create_booking_id():
    return 123

@pytest.fixture()
def read_csv_file_data():
    return "xyz"

def test_update_req_1(create_token):
    print("Booking ID -> ", create_booking_id)

def test_update_req_2(create_token, create_booking_id):
    print("Token ->", create_token)
    print("Booking ID -> ", create_booking_id)

def test_update_req_3(create_token, create_booking_id, read_csv_file_data):
    print("Token ->", create_token)
    print("Booking ID -> ", create_booking_id)
    print("Excel File ->", read_csv_file_data)
