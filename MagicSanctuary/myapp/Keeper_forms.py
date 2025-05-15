from django import forms
from .models import Keeper

class KeeperForm(forms.ModelForm):
    class Meta:
        model = Keeper
        fields = '__all__' # Or '__all__'