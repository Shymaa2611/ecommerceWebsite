from django import forms
from .models import user_profile

class userAccount(forms.ModelForm):
    class Meta:
        model=user_profile
        fields='__all__'