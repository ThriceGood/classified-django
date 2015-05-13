from django import forms
from .models import Advert


class AdvertForm(forms.ModelForm):
    class Meta:
        model = Advert
        # exclude user from from so an input is not
        # rendered by the template language
        # we will manually ad the user in the view file
        exclude = ['user']