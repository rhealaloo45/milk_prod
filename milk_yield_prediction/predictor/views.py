from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import PredictionForm
import joblib
import os

# Load the trained model
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "predictor/model/model.pkl")

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")

model = joblib.load(MODEL_PATH)

def predict_milk_production(request):
    if request.method == "POST":
        form = PredictionForm(request.POST)
        print("Hello")
        if form.is_valid():
            # Extract and convert form data
            age = int(form.cleaned_data["age"])
            breed = int(form.cleaned_data["breed"])
            health_status = int(form.cleaned_data["health_status"])
            housing_type = int(form.cleaned_data["housing_type"])
            vaccinated = 1 if form.cleaned_data["vaccinated"] else 0
            dewormed = 1 if form.cleaned_data["dewormed"] else 0

# }

            # Prepare data for the model
            input_data = [[breed, age, health_status, housing_type, vaccinated, dewormed]]
            print("Input Data for Prediction:", input_data)  # Debugging

            # Predict output
            try:
                prediction = model.predict(input_data)[0]
                print("Prediction Result:", prediction)  # Debugging
            except Exception as e:
                print("Prediction Error:", e)
                prediction = "Error in prediction"

            # Redirect to the result page with the prediction
            return redirect(reverse("result") + f"?prediction={prediction}")
    else:
        form = PredictionForm()

    return render(request, "predictor/predict.html", {"form": form})


def result(request):
    prediction = request.GET.get("prediction")
    return render(request, "predictor/result.html", {"prediction": prediction})
