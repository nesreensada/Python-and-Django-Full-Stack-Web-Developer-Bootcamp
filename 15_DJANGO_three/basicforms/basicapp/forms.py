from django import forms
from django.core import validators

class FormName(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    verify_email=forms.EmailField(label='enter email again')
    text=forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data=super().clean()
        email=all_clean_data['email']
        vmail=all_clean_data['verify_email']
        if email !=vmail:
            raise forms.ValidationError('Make email and vemail same')
