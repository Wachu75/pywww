from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, HTML, ButtonHolder
from django import forms
from main.models import UserProfile


class ContactForm(forms.Form): #ContactForm dziedziczy po wbudowanych django gotowych formularzy
    email = forms.EmailField(label="Adres email") # definiujemy z jakich pól skałeda się nasz formularz
    title = forms.CharField()  # title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'})) cdn..
    content = forms.CharField(widget=forms.Textarea) #cd.. w ten sposób dodajemy do naszych pól jako atrybut jakich klas chcemy użyć
    send_to_me = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'contact'
        self.helper.layout = Layout(
            Fieldset('Dane kontaktowe',
                     'email',
            ),
            Fieldset('Zawartość',
                     'title',
                     'content',
            ),
            Fieldset('Dodatkowe',
                     HTML("Zaznacz jeśli chcesz by wysłać kopię wiadomości do Ciebie"),
                     'send_to_me',
            ),
            ButtonHolder(
                Submit('submit', 'Wyślij', css_class='btn btn-primaty'),
                css_class="d-flex justify-content-end"
            )
        )

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user', 'bio']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'post'
            self.helper.form_action = 'profile'
            self.helper.add_input(Submit('submit','Wyślij'))
