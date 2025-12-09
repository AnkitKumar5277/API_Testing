import pytest

def method1():
    print("Hello World")

# Basic test suite jo ye check karta hai ki application ke main functions chal rahe hain ya nahi.
@pytest.mark.smoke
def test_method2():
    print("test1")
    assert 1-1 == 2

# Ye test ensure karta hai ki naye code changes ne purane (existing) features ko kharab toh
@pytest.mark.regression
def test_method3():
    print("test2")
    assert 1 + 1 == 2
