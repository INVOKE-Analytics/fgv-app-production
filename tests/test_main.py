from typing import Dict
from fastapi.testclient import TestClient
from main import app
from model_predict.predict import load_model

# API TEST
client = TestClient(app)
def test_count_pupa():
    response = client.get("/predict")
    assert response.status_code == 200, "Status code not 200"
    assert isinstance(response.json(), Dict), "Response is not json body"


# UNIT TEST

def test_load_model():

    model = load_model(model_path="/")
    assert isinstance(model, object)