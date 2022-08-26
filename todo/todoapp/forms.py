from . models import Task
from django import forms
class Tform(forms.ModelForm):
    class Meta:
        model=Task
        fields=['name','priority','Date']