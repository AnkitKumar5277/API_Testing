import pytest
import allure
@allure.title("Verify that create booking, with invalid data is working")
@allure.description("This Testcase check for the negative  create booking")
@pytest.mark.negative
def test_create_booking_negative_2():
    print("test2")
    assert 1 + 1 == 2

@pytest.mark.smoke
def test_method4():
    print("this is pytest")
    assert 1+1 == 0+2
