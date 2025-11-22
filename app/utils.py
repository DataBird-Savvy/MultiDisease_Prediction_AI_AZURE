
import torch
import torch.nn as nn
from torchvision.models import resnet50, ResNet50_Weights
import albumentations as A
from albumentations.pytorch import ToTensorV2
from PIL import Image
import numpy as np
from config import CLASS_NAMES
from logger import logger
from exception import XRAYException
import sys
from config import WEIGHT_PATH





class ResNet50MultiLabel(nn.Module):
    def __init__(self, n_classes):
        super().__init__()
        self.model = resnet50(weights=ResNet50_Weights.IMAGENET1K_V2)
        in_features = self.model.fc.in_features
        self.model.fc = nn.Linear(in_features, n_classes)

    def forward(self, x):
        return self.model(x)


transform = A.Compose([
    A.Resize(224, 224),
    A.Normalize(),
    ToTensorV2()
])


def load_model(weight_path, device):
    try:
        logger.info("Loading model...")
        model = ResNet50MultiLabel(len(CLASS_NAMES))

        state_dict = torch.load(WEIGHT_PATH, map_location=device, weights_only=False)

        model.load_state_dict(state_dict)
        model.to(device)
        model.eval()

        logger.info("Model loaded successfully.")
        return model

    except Exception as e:
        logger.error(f"Failed to load model: {str(e)}")
        raise XRAYException(e, sys)


def predict_image(model, image_path, device):
    try:
        logger.info(f"Predicting image: {image_path}")

        img = np.asarray(Image.open(image_path).convert("RGB"))
        tensor = transform(image=img)["image"].unsqueeze(0).to(device)

        with torch.no_grad():
            outputs = model(tensor)
            probs = torch.sigmoid(outputs)[0].cpu().numpy()

        preds = {cls: float(p) for cls, p in zip(CLASS_NAMES, probs)}

        logger.info("Prediction completed.")
        return preds

    except Exception as e:
        logger.error(f"Prediction failed: {str(e)}")
        raise XRAYException(e, sys)
