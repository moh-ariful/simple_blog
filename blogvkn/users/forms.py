from django import forms
from django.contrib.auth import authenticate
# New


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label="Username")
    password = forms.CharField(
        max_length=100, label="Password", widget=forms.PasswordInput)

    def clean(self):  # Membersihkan data pada form demi security
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                raise forms.ValidationError("Username or Password no correct!")
            return super(LoginForm, self).clean()
