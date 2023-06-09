import streamlit as st
from PIL import Image
from fgv_app_production.model_predict.predict import PredictPupa
from pathlib import Path

st.title("FGV-Pupa Detector")
with st.sidebar:
    pupa_image = st.file_uploader(
        label="Upload the pupa image here",
        type=["png", "jpg"],
        # accept_multiple_files=True,
        key="pupa-image",
    )
    detector_button = st.button(
        label="Detect",
        key="detect-pupa-button",
    )


if detector_button:
    try:
        # input image
        in_content = Image.open(pupa_image)
    except Exception as readError:
        st.error(f"Error:{readError}")

    model = PredictPupa(img_path=in_content)
    pupa_output = model.predict_pupa()
    df = pupa_output.pandas().xyxy[0]

    if "pupa-image" in st.session_state:
        st.image(image=f"../fgv_app_production/inference_out/image0.jpg")
        st.table(df)
