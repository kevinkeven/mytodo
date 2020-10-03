from django import forms
from .models import Todo
from django.contrib.auth import get_user_model
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit

class TodoCreationForm(forms.ModelForm):
    owner = forms.ModelChoiceField(
        queryset = get_user_model().objects.all(),
        widget = forms.HiddenInput,
        disabled = True,
        required=False,
    )
    class Meta:
        model = Todo
        fields = ('owner', 'title', 'description',)

class TodoActiveForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Submit('submit', 'YES', css_class='btn btn-block btn-dark')
        )
    class Meta:
        model = Todo
        fields = ('active',)

class TodoUpdateForm(forms.ModelForm):
    owner = forms.ModelChoiceField(
        queryset = get_user_model().objects.all(),
        widget = forms.HiddenInput,
        disabled = True,
        required=False,
    )
    class Meta:
        model = Todo
        fields = ('title', 'description', 'active')