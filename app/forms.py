from django import forms

class NewDogTagForm(forms.Form):
    owner_name = forms.CharField(min_length=1)
    dog_name = forms.CharField(min_length=1)
    dog_birthday = forms.DateField()
