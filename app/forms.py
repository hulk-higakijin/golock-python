from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

class PostForm(forms.Form):
  year = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(2021)])
  text = forms.CharField(max_length=30, label="語呂合わせ（文）")
  supplement = forms.CharField(max_length=100, label="説明")
