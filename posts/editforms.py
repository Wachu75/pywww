from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from django import forms
from posts.models import Post


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'published', 'sponsored']
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
        self.helper.form_action = 'edit'
        self.helper.layout = Layout(
            Fieldset(
                'Dodaj post',
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
