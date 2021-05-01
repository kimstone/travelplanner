from django import forms
from django.forms import ModelForm
from .models import *

class BucketListForm(forms.ModelForm):

    class Meta:
        model = BucketList
        fields = '__all__'