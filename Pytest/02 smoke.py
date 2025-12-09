import pytest

def method1():
    print("Hello World")

@pytest.mark.smoke
def test_method2():
    print("test1")
    assert 1-1 == 2

@pytest.mark.regression
def test_method3():
    print("test2")
    assert 1 + 1 == 2
  
# method1() ek normal function hai jo "Hello World" print karta hai. 
  # test_method2() ek smoke test hai jo fail hoga kyunki 1-1 == 2 galat hai.
  # test_method3() ek regression test hai jo pass hoga kyunki 1+1 == 2 sahi hai. PyTest test cases detect karta hai.
