from django import forms
from .models import TitanicDb

class TitanicForm(forms.ModelForm):
    class Meta:
        model = TitanicDb
        fields = ['pclass', 'sex', 'age', 'sibhp', 'parch', 'fare', 'mbarked', 'title']

