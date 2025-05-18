# School Connectivity Predictor

A machine learning API that predicts school connectivity levels based on geographical and infrastructure data.

## Overview

This project implements a machine learning model that predicts school connectivity levels (Low, Medium, High) based on the following features:
- Latitude
- Longitude
- Bandwidth (Mbps)
- Urban/Rural location (0 or 1)

## Project Structure

- `generate_data.py` - Generates synthetic training data
- `train_model.py` - Trains and saves the Random Forest model
- `app.py` - FastAPI application that serves predictions
- `requirements.txt` - Project dependencies
- `Dockerfile` - Container configuration

## Installation

1. Clone the repository
2. Install dependencies:
```sh
pip install -r requirements.txt
```

## Usage

### Local Development

1. Generate the training data:
```sh
python generate_data.py
```

2. Train the model:
```sh
python train_model.py
```

3. Start the API server:
```sh
uvicorn app:app --reload
```

### Docker Deployment

Build and run the Docker container:
```sh
docker build -t school-connectivity .
docker run -p 8000:8000 school-connectivity
```

## API Endpoints

### POST /predict

Make predictions with the following JSON format:
```json
{
    "latitude": 45.0,
    "longitude": 90.0,
    "bandwidth_mbps": 5.0,
    "is_urban": 1
}
```

## Dependencies

- FastAPI
- Uvicorn
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Pydantic