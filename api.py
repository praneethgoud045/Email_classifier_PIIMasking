from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from utils import mask_pii

# Load model
model = joblib.load('saved_models/email_classifier.pkl')

# Define FastAPI app
app = FastAPI()

# Request schema
class EmailRequest(BaseModel):
    email_body: str

# API Endpoint
@app.post("/classify-email")
def classify_email_api(request: EmailRequest):
    masked_email, masked_entities = mask_pii(request.email_body)
    predicted_category = model.predict([masked_email])[0]

    return {
        "input_email_body": request.email_body,
        "list_of_masked_entities": masked_entities,
        "masked_email": masked_email,
        "category_of_the_email": predicted_category
    }
