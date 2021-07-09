from django import forms  
from .models import Transitions  
class TransitionsForm(forms.ModelForm):  
    class Meta:  
        model = Transitions
        fields = "__all__"