from django import forms
from .models import profile


class profileForm(forms.ModelForm):
    class Meta:
        model = profile
        # exclude user from from so an input is not
        # rendered by the template language
        # we will manually ad the user in the view file
        exclude = ['user']