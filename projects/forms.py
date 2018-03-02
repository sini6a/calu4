from django import forms

class NewDonationForm(forms.Form):
    amount_to_Donate = forms.IntegerField(min_value=1)

