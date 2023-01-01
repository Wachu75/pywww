from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from django import forms
from django.urls import reverse
from posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'published', 'sponsored', 'image', "tags"]
        labels = {
            "title": "Tytuł-0",
            "content": "Treść",
            "published": "Opublikowany",
            "sponsored": "Sponsorowany"
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'add'
        self.helper.layout = Layout(
            Fieldset(
                'Dodaj post',
                'title',
                'content',
                'published',
                'sponsored',
                'image',
                'tags',
            ),
            ButtonHolder(
                Submit('submit', 'Dodaj', css_class="btn btn-primary"),
                css_class="d-flex justify-content-end"
            )
        )

class PostFormEdit(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'published', 'sponsored']
        labels = {
            "title": "Tytuł-1",
            "content": "Treść",
            "published": "Opublikowany",
            "sponsored": "Sponsorowany"
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        #self.helper.form_action = 'list' #'../save' #reverse('../save', args=[post_id]) old reverse('url_name', args=[self.instance.id])
        self.helper.layout = Layout(
            Fieldset(
                'Edycja posta',
                'title',
                'content',
                'published',
                'sponsored',
            ),
            ButtonHolder(
                Submit('submit', 'Edytuj', css_class="btn btn-primary"),
                css_class="d-flex justify-content-end"
            )
        )

class PostFormNotEdit(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'published', 'sponsored']
        labels = {
            "title": "Tytuł-2",
            "content": "Treść",
            "published": "Opublikowany",
            "sponsored": "Sponsorowany"
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'edit'
        self.helper.layout = Layout(
            Fieldset(
                'Edycja posta',
                'title',
                'content',
                'published',
                'sponsored',
            )
        )