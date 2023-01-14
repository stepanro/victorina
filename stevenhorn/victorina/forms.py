from django import forms

class LoginForm(forms.Form):
    game_in_company = forms.CharField(label='game_in_company', max_length=10)
    game_in_online = forms.CharField(label='game_in_company', max_length=10)
    name = forms.CharField(label='Name', max_length=100)