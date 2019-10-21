from django.contrib.auth.models import User
from django import forms


class ProfileForm(forms.ModelForm):

    occupation = forms.CharField()
    bio = forms.CharField()
    location = forms.CharField()

    class Meta:
        model = User
        fields = ('occupation', 'bio', 'location')
