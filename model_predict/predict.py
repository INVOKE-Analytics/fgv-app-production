from pathlib import Path
from yolov5.detect import run
import torch


class PredictPupa:
    def __init__(self, img_path):
        self.IMG_SIZE = (1024, 1024)
        self.CONF_THRESHOLD: float = 0.20
        self.model_output_path = Path("../fgv_app_production/model_output")
        self.MODEL_WEIGHT_PATH: str = self.model_output_path / "best_100.pt"
        # img_path: str = model_output_path / "ulat_test.png"
        self.result_path = str(self.model_output_path)
        self.img_path = img_path

    def predict_pupa(self):
        # output = run(
        #     weights=self.MODEL_WEIGHT_PATH,
        #     imgsz=self.IMG_SIZE,
        #     conf_thres=self.CONF_THRESHOLD,
        #     source=self.img_path,
        #     project=self.result_path,
        #     save_txt=True,
        #     save_conf=True,
        #     save_crop=True,
        # )

        model = torch.hub.load(
            repo_or_dir="../fgv_app_production/yolov5",
            model="custom",
            source="local",
            path=self.MODEL_WEIGHT_PATH,
        )
        result = model(self.img_path)
        return result


if __name__ == "__main__":
    # $ python -m model_predict.predict
    pred = PredictPupa(img_path="../fgv_app_production/model_output/ulat_test.png")
    pred.predict_pupa()
