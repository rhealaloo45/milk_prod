# Create your views here.
from django.shortcuts import render
from .forms import MilkYieldForm
from .utils import predict_milk_yield

def predict_view(request):
    if request.method == "POST":
        form = MilkYieldForm(request.POST)
        if form.is_valid():
            # Extract the last 10 days of input data
            input_data = [
                form.cleaned_data['day_1'],
                form.cleaned_data['day_2'],
                form.cleaned_data['day_3'],
                form.cleaned_data['day_4'],
                form.cleaned_data['day_5'],
                form.cleaned_data['day_6'],
                form.cleaned_data['day_7'],
                form.cleaned_data['day_8'],
                form.cleaned_data['day_9'],
                form.cleaned_data['day_10'],
            ]
            
            # Make prediction
            predicted_yield = predict_milk_yield(input_data)
            
            return render(request, 'prediction_result.html', {
                'predicted_yield': predicted_yield
            })
    else:
        form = MilkYieldForm()
    
    return render(request, 'predict_form.html', {'form': form})

