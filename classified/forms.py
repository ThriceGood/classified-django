from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# make overriding user registration form
# extends UserCreationForm
class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    # what model to apply to form and what fields
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    # save function overrides super save functiom to add extra
    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        # cleaned data is data gotten from form
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user