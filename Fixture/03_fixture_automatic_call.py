import pytest

@pytest.fixture()
def launch_browser():
    print("Browser Launched")
    return

@pytest.fixture()
def close_browser():
    print("Browser Closed")
    return

def test_selenium(launch_browser, close_browser):
    print("Do Tc")

# Jab `test_selenium()` run hota hai, tab ye dono fixtures automatically call ho jaate hain. 
