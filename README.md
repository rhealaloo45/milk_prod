# milk_prod: milk-yield prediction service

A small Django web service that predicts a cow's daily milk production, in litres, from six facts about the animal: breed, age, health status, housing type, and whether it is vaccinated and dewormed. The model is a scikit-learn `RandomForestRegressor`, saved as `predictor/model/model.pkl`.

This repo is one part of a cattle-management system built for Nareshwadi Learning Centre (June 2024 – June 2025). The other web part is [nareshwadi-web](https://github.com/rhealaloo45/nareshwadi-web).

**Demo video of the app:** [watch on Google Drive](https://drive.google.com/file/d/11BQ3Qv-VxpQNHI4r4o9K69amzxmMTIhk/view)

## The wider system

The full system included a Random Forest that predicted disease and milk-yield trends from each cow's last 10 days of milk records, at 94% accuracy, along with 7-day milk production analytics. The training notebook and the evaluation behind the 94% figure are not in this repo. What's here is the web service that serves the attribute-based yield model.

## How it works

1. `GET /` shows a form (`predictor/forms.py`) with these fields:
   - breed: HF cross, Jersey cross or Gir
   - age in years
   - health status: Fair, Good or Excellent
   - housing type: semi tied-up, open grazing or loose housing
   - vaccinated (yes/no)
   - dewormed (yes/no)
2. On submit, `predictor/views.py` encodes the fields in the order the model was trained on (`Breed, Age, HealthStatus, HousingType, Vaccinated, Dewormed`) and calls `model.predict`.
3. The view redirects to `/result/`, which shows the predicted daily production in litres.

`predictor/utils.py` also has an experimental LSTM helper that would forecast the next day's yield from the last 10 days. It expects `lstm_milk_yield_model.h5` and `scaler.pkl`. Those files are not in the repo and no view calls the helper yet.

## Stack

Python, Django 4.1, scikit-learn 1.6.1 (Random Forest regression), joblib, SQLite.

## Run it

The model was pickled with scikit-learn 1.6.1, so install that exact version to load it.

```bash
cd milk_yield_prediction
python -m venv .venv && source .venv/bin/activate
pip install "django>=4.1,<5" "scikit-learn==1.6.1" joblib numpy
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000, fill in the form and submit.

## Project structure

```
milk_yield_prediction/
├── milk_yield_project/        Django settings and root URLs
└── predictor/
    ├── forms.py               the six input fields and their encodings
    ├── views.py               loads model.pkl once, predicts, shows the result
    ├── utils.py               experimental 10-day LSTM helper (not wired up)
    ├── model/model.pkl        trained RandomForestRegressor
    └── templates/predictor/   form and result pages
```
