from django import forms

class NewDogTagForm(forms.Form):
    owner_name = forms.CharField(min_length=1)
    dog_name = forms.CharField(min_length=1)
    dog_birthday = forms.DateField()
    owner_address = forms.CharField(min_length=1)
    dog_color = forms.CharField(min_length=1)