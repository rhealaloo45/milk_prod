from django import forms

class MilkYieldForm(forms.Form):
    day_1 = forms.FloatField(label="Day 1 Yield")
    day_2 = forms.FloatField(label="Day 2 Yield")
    day_3 = forms.FloatField(label="Day 3 Yield")
    day_4 = forms.FloatField(label="Day 4 Yield")
    day_5 = forms.FloatField(label="Day 5 Yield")
    day_6 = forms.FloatField(label="Day 6 Yield")
    day_7 = forms.FloatField(label="Day 7 Yield")
    day_8 = forms.FloatField(label="Day 8 Yield")
    day_9 = forms.FloatField(label="Day 9 Yield")
    day_10 = forms.FloatField(label="Day 10 Yield")
