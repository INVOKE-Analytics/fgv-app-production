from pathlib import Path
from yolov5.detect import run


def predict_pupa():
    IMG_SIZE = (1024, 1024)
    CONF_THRESHOLD: float = 0.20
    model_output_path = Path("../fgv_app_production/model_output")
    MODEL_PATH: str = model_output_path / "best_100.pt"
    img_path: str = model_output_path / "ulat_test.png"
    result_path = str(model_output_path)
    output = run(
        weights=MODEL_PATH,
        imgsz=IMG_SIZE,
        conf_thres=CONF_THRESHOLD,
        source=img_path,
        project=result_path,
        save_txt=True,
        save_conf=True,
        save_crop=True,
    )

    return output


if __name__ == "__main__":
    predict_pupa()
