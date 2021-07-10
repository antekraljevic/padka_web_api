from django import forms  
from .models import Reactions, Transitions, Music  
class TransitionsForm(forms.ModelForm):  
    class Meta:  
        model = Transitions
        fields = "__all__"

class ReactionsForm(forms.ModelForm):  
    class Meta:  
        model = Reactions
        fields = "__all__"

class MusicForm(forms.ModelForm):  
    class Meta:  
        model = Music
        fields = "__all__"