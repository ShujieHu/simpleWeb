# users/forms.py

from django.contrib.auth.forms import UserCreationForm
from django import forms

# This is the class for creating new users


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)


# This is the corresponding form for country field
class CountryForm(forms.Form):
    country = forms.CharField(label='country', max_length=100)
