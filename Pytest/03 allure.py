# pytest main.py --alluredir=reports
# allure serve reports

import pytest
import allure

@allure.title("Verify that create booking, with valid data is working")
@allure.description("This Testcase check for the positive create booking")
@pytest.mark.positive
def test_create_booking_positive():
    print("test1")
    assert 1-1 == 2

@allure.title("Verify that create booking, with invalid data is working")
@allure.description("This Testcase check for the negative  create booking")

@pytest.mark.negative
def test_create_booking_negative_1():
    print("test2")
    assert 1 + 1 == 2


@allure.title("Verify that create booking, with invalid data is working")
@allure.description("This Testcase check for the negative  create booking")
@pytest.mark.negative
def test_create_booking_negative_2():
    print("test3")
    assert 1 + 1 == 2

# Yeh PyTest aur Allure ka use karke likha gaya test automation code hai jo **create booking feature** ko test karta hai.
# `test_create_booking_positive()` ek **positive test case** hai, jisme valid data diya gaya hai lekin `assert 1-1 == 2` galat hai, isliye test **fail** hoga.
# `test_create_booking_negative_1()` aur `test_create_booking_negative_2()` do **negative test cases** hain, jo invalid data ke saath test karte hain. Inmein `assert 1+1 == 2` diya gaya hai, jo sahi hai, isliye ye dono test cases **pass** honge.
# Allure ke `@title` aur `@description` decorators test reports ko detailed aur readable banate hain.

