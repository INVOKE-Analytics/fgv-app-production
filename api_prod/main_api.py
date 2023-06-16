from fastapi import FastAPI, Depends, UploadFile, File, HTTPException, status
from model_predict.predict import PredictPupa
import sys, threading
import os
from mangum import Mangum
import uvicorn

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)

app = FastAPI()


@app.get("/")
async def root():
    return {"Health test": "Good!"}


@app.post("/predict")
async def predict_metisa(pupa_img: UploadFile = File(...)):
    try:
        # NOTE: Current use
        content = pupa_img.file.read()
        with open(pupa_img.filename, "wb") as f:
            f.write(content)

        # read_img = pupa_img.file.read()
        # with open(pupa_img.filename, "rb") as f:
        #     img_bytes = f.read()
        # content = Image.open(io.BytesIO(img_bytes))

    except Exception as readError:
        raise {"readError message": readError}

    # finally:
    #     f.close()

    try:
        pred = PredictPupa(img_path=pupa_img.filename)
        output = pred.predict_pupa()
    except Exception as errorRecog:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error: {errorRecog}",
        )
    finally:
        os.remove(f"../fgv_app_production/{pupa_img.filename}")

    return {
        "filename": pupa_img.filename,
        "content-type": pupa_img.content_type,
        "image-bbox": output.pandas().xyxy[0].to_json(orient="records"),
    }


if __name__ == "__main__":
    uvicorn.run("main_api:app", port=8000, host="127.0.0.1")
else:
    handler = Mangum(app)
