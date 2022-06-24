from django import forms
from .models import Candidate

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ('name', 'phone', 'email', 'gender', 'career')
        labels = {
            'name':'Name',
            'email':'Email',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Your phone'}),
            'email': forms.TextInput(attrs={'placeholder': 'Your email'}),
        }

    def __init__(self, *args, **kwargs):
        super(CandidateForm, self).__init__(*args, **kwargs)
        self.fields['gender'].choices = [("", "Select a gender"),] + list(self.fields['gender'].choices)[1:]
        self.fields['career'].empty_label = "Select an option"
        self.fields['email'].required = True
