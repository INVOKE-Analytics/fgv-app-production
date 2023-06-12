from pathlib import Path
import torch


class PredictPupa:
    def __init__(self, img_path):
        self.IMG_SIZE = (1024, 1024)
        self.CONF_THRESHOLD: float = 0.20
        self.project_path = Path("../fgv_app_production")
        self.model_output_path = self.project_path / "model_output"
        self.MODEL_WEIGHT_PATH: str = self.project_path / "model_output/best_100.pt"
        self.result_path = str(self.model_output_path)
        self.img_path = img_path

    def predict_pupa(self):
        yolo_path = Path("./yolov5")
        assert yolo_path.exists() == True, "Yolov5 is not exist"
        model = torch.hub.load(
            repo_or_dir="ultralytics/yolov5",
            model="custom",
            source="github",
            path=self.MODEL_WEIGHT_PATH,
        )
        result = model(self.img_path)
        result.save(save_dir="../fgv_app_production/inference_out/", exist_ok=True)
        return result


if __name__ == "__main__":
    # $ python -m model_predict.predict
    pred = PredictPupa(img_path="../fgv_app_production/model_output/ulat_test.png")
    pred.predict_pupa()
