import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


WEIGHT_PATH = os.path.normpath(os.path.join(BASE_DIR, "..", "model", "best_resnet50.pth"))
CLASS_NAMES = [
    "Atelectasis", "Cardiomegaly", "Effusion", "Infiltration",
    "Mass", "Nodule", "Pneumonia", "Pneumothorax",
    "Consolidation", "Edema", "Emphysema", "Fibrosis",
    "Pleural_Thickening", "Hernia",
]