from fastapi import FastAPI, UploadFile, File
import tempfile
import os

from ml.training.trainer import predict_voice_sample

app = FastAPI(title="VOXSHIELD API")


@app.get("/")
def root():
    return {
        "message": "VOXSHIELD API is running",
        "status": "online"
    }


@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    suffix = os.path.splitext(file.filename)[1]

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp:
        temp.write(await file.read())
        temp_path = temp.name

    try:
        result = predict_voice_sample(temp_path)

        return {
            "filename": file.filename,
            "authentic_probability": result["authentic_probability"],
            "synthetic_probability": result["synthetic_probability"],
            "speaker_match": result["speaker_match"],
            "risk_level": result["risk_level"],
            "decision": result["decision"]
        }

    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)
