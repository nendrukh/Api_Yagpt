from main import app

from fastapi.testclient import TestClient

test_client = TestClient(app)


def test_empty_prompt():
    response = test_client.post("/ask_gpt", json={"gpt_role": "Переводчик"})
    assert response.status_code != 200


def test_successful_response():
    response = test_client.post("/ask_gpt", json={"prompt": "Привет", "gpt_role": "Друг"})
    response_json = response.json()
    assert response.status_code == 200
    assert response_json["result"]
    assert response_json["code"] == "OK"


def test_prompt_without_role():
    response = test_client.post("/ask_gpt", json={"prompt": "Привет"})
    response_json = response.json()
    assert response.status_code == 200
    assert response_json["code"] == "OK"
