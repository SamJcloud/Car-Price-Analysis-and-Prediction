#  Car Price Prediction API

A machine learning-based FastAPI service to predict the selling price of used cars. The model considers various car features such as fuel type, seller type, engine specs, and mileage to generate accurate predictions. This project is production-ready and supports deployment via FastAPI and Streamlit.

---

##  Features

- RESTful API using **FastAPI**
- Input validation with **Pydantic**
- Robust model prediction with **Random Forest Regressor**
- CORS-enabled for integration with frontends like **Streamlit**
- Error handling with detailed tracebacks
- Trained model and feature order stored via **joblib**

---

##  Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/SamJcloud/Car-Price-Analysis-and-Prediction.git
cd Car-Price-Analysis-and-Prediction
```
## Create and Activate a Virtual Environment
```python
python -m venv venv
venv\Scripts\activate
```
## Install Dependencies
```python
pip install -r requirements.txt
```
## Start the FastAPI Server
```python
uvicorn main:app --reload
```
Open your browser at: http://127.0.0.1:8000/docs to access the Swagger UI for API testing.

## API Endpoint
### /predict [POST]
Request Body:
```json
{
  "km_driven": 45000,
  "fuel": "Petrol",
  "seller_type": "Dealer",
  "transmission": "Manual",
  "owner": "First Owner",
  "mileage_km_ltr_kg": 18.5,
  "engine": 1197,
  "max_power": 82.0,
  "seats": 5,
  "brand": "Maruti",
  "car_age": 5
}
```
### Response:
```json
{
  "prediction": 375000.0
}
```
