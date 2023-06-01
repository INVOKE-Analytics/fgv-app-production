from main import count_pupa
from typing import Dict
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
def test_count_pupa():
    response = client.get("/predict")
    assert response.status_code == 200, "Status code not 200"
    assert isinstance(response.json(), Dict), "Response is not json body"


