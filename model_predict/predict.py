import torch 


def load_model(model_path:str):

    uploaded_model = torch.load(model_path)
    return uploaded_model