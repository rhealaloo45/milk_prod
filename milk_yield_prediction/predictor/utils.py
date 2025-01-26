import numpy as np
import joblib
from tensorflow.keras.models import load_model

# Load the trained model and scaler
MODEL_PATH = 'predictor/model/lstm_milk_yield_model.h5'
SCALER_PATH = 'predictor/model/scaler.pkl'

model = load_model(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

def predict_milk_yield(input_data):
    """
    Predict milk yield based on the last 10 days of input data.

    Parameters:
        input_data (list or numpy array): A list or array of the last 10 days of milk yield.

    Returns:
        float: Predicted milk yield.
    """
    # Ensure the input data is in the correct shape
    input_data = np.array(input_data).reshape(-1, 1)
    
    # Scale the data
    scaled_input = scaler.transform(input_data)
    scaled_input = scaled_input.reshape(1, 10, 1)  # Shape for LSTM: [samples, time steps, features]
    
    # Make prediction
    scaled_prediction = model.predict(scaled_input)
    
    # Reverse scaling
    actual_prediction = scaler.inverse_transform(scaled_prediction.reshape(-1, 1))
    return actual_prediction[0][0]
