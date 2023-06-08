from fastapi import FastAPI
from typing import Dict
from model_predict.predict import predict_pupa

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello-wordl!"}


@app.get("/predict")
async def count_pupa() -> Dict[str, int]:
    """
    Recognize the type of the pupa and
    returning the amount of the class.
    """

    # LOAD MODEL
    output = predict_pupa()

    # EVAL
    # output = model.eval()

    # COUNT CLASS
    amount_c1 = 10
    amount_c2 = 10
    amount_c3 = 10
    amount_c4 = 10
    amount_c5 = 10
    amount_c6 = 10
    amount_c7 = 10
    amount_c8 = 10

    return {
        "amount_class_1": amount_c1,
        "amount_class_2": amount_c2,
        "amount_class_3": amount_c3,
        "amount_class_4": amount_c4,
        "amount_class_5": amount_c5,
        "amount_class_6": amount_c6,
        "amount_class_7": amount_c7,
        "amount_class_8": amount_c8,
    }
