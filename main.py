# plant_disease_api/main.py
from fastapi import FastAPI, File, UploadFile
from PIL import Image
from model.model_loader import load_model, predict
from utils.treatment_data import disease_treatment

app = FastAPI()
model = load_model()

@app.get("/")
def home():
    return {"message": "Plant Disease API running."}

@app.post("/predict/")
async def predict_image(file: UploadFile = File(...)):
    image = Image.open(file.file).convert("RGB")
    prediction = predict(model, image)
    advice = disease_treatment.get(prediction, {
        "treatment": "No data available",
        "prevention": "No data available"
    })
    return {
        "disease": prediction,
        "treatment": advice["treatment"],
        "prevention": advice["prevention"]
    }
