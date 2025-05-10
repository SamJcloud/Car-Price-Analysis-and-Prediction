import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import joblib
from pydantic import BaseModel,Field
import traceback

app = FastAPI(title="Car Price Prediction API", description="API for predicting car prices based on various features.", version="1.0")

app.add_middleware(
     CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CarPricePrediction(BaseModel):
    km_driven: int = Field(..., ge=0, description="Total kilometers driven")
    fuel: str = Field(..., pattern="^(Petrol|Diesel|CNG|LPG)$", description="Type of fuel used")
    seller_type: str = Field(..., pattern="^(Dealer|Individual)$", description="Type of seller")
    transmission: str = Field(..., pattern="^(Manual|Automatic)$", description="Type of transmission")
    owner: str = Field(..., pattern="^(First Owner|Second Owner|Third Owner|Fourth & Above Owner)$", description="Owner type")
    mileage_km_ltr_kg: float = Field(..., ge=0, description="Mileage of the car in km/l")
    engine: float = Field(..., ge=0, description="Engine capacity in cc")
    max_power: float = Field(..., ge=0, description="Maximum power of the car in bhp")
    seats: float = Field(..., ge=0, description="Number of seats in the car")
    brand: str = Field(..., pattern="^(Maruti|Hyundai|Honda|Toyota|Ford|Chevrolet|Nissan|Volkswagen|Renault|Tata)$", description="Brand of the car")
    car_age: int = Field(..., ge=0, le=100, description="Age of the car in years")

try:
    model = joblib.load("car_price_model.joblib")
    print("Model loaded successfully!")
except Exception as e:
    print("Error loading model:", str(e))
    traceback.print_exc()


@app.get("/")   
def read_root():
    return {"message": "Car Price Prediction API is running."}

@app.post("/predict")
def predict(car: CarPricePrediction):
    try:
        data = {
            'km_driven':car.km_driven,
            'fuel':car.fuel,
            'seller_type':car.seller_type,
            'transmission':car.transmission,
            'owner':car.owner,
            'mileage(km/ltr/kg)': car.mileage_km_ltr_kg,
            'engine':car.engine,
            'max_power':car.max_power,
            'seats':car.seats,
            'brand':car.brand,
            'car_age':car.car_age
        }
        df = pd.DataFrame([data], columns=['km_driven', 'fuel', 'seller_type', 'transmission', 'owner', 'mileage(km/ltr/kg)', 'engine','max_power','seats','brand','car_age'])
        prediction = model.predict(df)[0]
        return {"prediction": round(prediction,2)}
    except Exception as e:
        return {"error": str(e)}
    

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000,)