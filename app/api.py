from fastapi import FastAPI, HTTPException
import joblib
import pandas as pd
from pydantic import BaseModel

app = FastAPI()
model = joblib.load("../models/preprocessor_churn.pkl")

class ChurnData(BaseModel):
    Age: int
    Gender: str
    Tenure: int
    Usage_Frequency: int
    Support_Calls: int
    Payment_Delay: int
    Subscription_Type: str
    Contract_Length: str
    Total_Spend: int
    Last_Interaction: int

@app.post("/predict/")
def predict_churn(features: ChurnData):
    try:
        df = pd.DataFrame([features.dict()])
        prediction = model.predict(df)
        return {"churn": bool(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))