# plant_disease_api/twilio_webhook.py
from fastapi import FastAPI, Form, File, UploadFile
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
import requests
from model.model_loader import load_model, predict
from PIL import Image
from io import BytesIO
from twilio.twiml.messaging_response import MessagingResponse

app = FastAPI()

model = load_model()

@app.post("/whatsapp")
async def whatsapp_webhook(
    MediaUrl0: str = Form(None),
    From: str = Form(None),
):
    response = MessagingResponse()

    if MediaUrl0:
        image_bytes = requests.get(MediaUrl0).content
        image = Image.open(BytesIO(image_bytes)).convert("RGB")

        disease = predict(model, image)

        # Add basic treatment/prevention (you can expand later)
        treatment_dict = {
            "Tomato___Tomato_mosaic_virus": {
                "treatment": "Remove and destroy infected plants.",
                "prevention": "Disinfect tools. Avoid tobacco use near plants."
            },
            # Add other diseases...
        }

        result = treatment_dict.get(disease, {
            "treatment": "No data available.",
            "prevention": "No data available."
        })

        response.message(
            f"🌿 Disease Detected: {disease}\n\n"
            f"🧪 Treatment: {result['treatment']}\n"
            f"🛡️ Prevention: {result['prevention']}"
        )
    else:
        response.message("Please send a photo of the plant or leaf showing the disease.")

    return PlainTextResponse(str(response))
