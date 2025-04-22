import pytest
import requests

BASE_URL = "http://localhost:8080"
TEST_USER = "octocat"

def test_gist_endpoint():
    response = requests.get(f"{BASE_URL}/{TEST_USER}")
    assert response.status_code == 200
    
    gists = response.json()
    assert isinstance(gists, list)

def test_pagination():
    response = requests.get(f"{BASE_URL}/{TEST_USER}?page=1&per_page=3")
    assert response.status_code == 200
    
    gists = response.json()
    print("----", len(gists) )
    assert isinstance(gists, list)
    assert len(gists) == 3


def test_invalid_user():
    non_existing_user = "invaliduserdoesnotexist"
    response = requests.get(f"{BASE_URL}/{non_existing_user}")
    assert response.status_code == 404
    assert response.json()['message'] == "Not Found"
