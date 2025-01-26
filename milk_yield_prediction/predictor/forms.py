from django import forms

class PredictionForm(forms.Form):
    age = forms.IntegerField(label="Cattle Age", min_value=1, help_text="Enter the age of the cattle in years.")
    
    breed = forms.ChoiceField(
        label="Breed",
        choices=[
            ("0", "hfC"), 
            ("1", "jerseyC"), 
            ("2", "gir")
        ],
        help_text="Select the breed of the cattle."
    )
    
    health_status = forms.ChoiceField(
        label="Health Status",
        choices=[
            ("0", "Fair"), 
            ("1", "Excellent"), 
            ("2", "Good")
        ],
        help_text="Select the current health status of the cattle."
    )
    
    housing_type = forms.ChoiceField(
        label="Housing Type",
        choices=[
            ("0", "Semi tied-up"), 
            ("1", "Open grazing"), 
            ("2", "Loose housing")
        ],
        help_text="Select the type of housing used for the cattle."
    )
    
    vaccinated = forms.BooleanField(
        label="Vaccinated",
        required=False,
        help_text="Check if the cattle is vaccinated."
    )
    
    dewormed = forms.BooleanField(
        label="Dewormed",
        required=False,
        help_text="Check if the cattle has been dewormed."
    )
