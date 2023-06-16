import streamlit as st
from PIL import Image
from model_predict.predict import PredictPupa
from pathlib import Path

st.title("FGV-Pupa Detector 🐛")
with st.sidebar:
    pupa_image = st.file_uploader(
        label="👇 Upload the pupa image here",
        type=["png", "jpg"],
        # accept_multiple_files=True,
        key="pupa-image",
    )

if st.session_state["pupa-image"]:
    in_content = Image.open(pupa_image)
    with st.expander("See image input"):
        st.image(in_content, caption=pupa_image.name)
    detector_button = st.button(
        label="Detect the pupa!",
        key="detect-pupa-button",
    )

    if st.session_state["detect-pupa-button"]:
        model = PredictPupa(img_path=in_content)
        pupa_output = model.predict_pupa()
        df = pupa_output.pandas().xyxy[0]
        df = df[["name", "class", "confidence"]]

        df_count = df.groupby(["name"])["name"].count().to_frame()

        print("DEBUGGG", type(df_count))
        df_count.rename(columns={"name": "Amount", "": "class"}, inplace=True)

        with st.empty():
            st.success("Detection succeed")
        st.balloons()

        with st.expander("See image output"):
            st.image(image=f"../fgv_app_production/inference_out/image0.jpg")
        col1, col2 = st.columns(2)
        with col1:
            with st.expander("Detected"):
                st.table(df)
        with col2:
            with st.expander("Counted"):
                st.table(df_count)

else:
    st.warning("No image uploaded.")
