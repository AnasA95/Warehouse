from django import forms
from .models import User


class LoginForm(forms.Form):
    username = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.get(id=username)
        if not user:
            raise forms.ValidationError("User does not exist in our db!")
        else:
            if not user.get(password=self.cleaned_data['password']):
                raise forms.ValidationError("Wrong password!")
        return username
