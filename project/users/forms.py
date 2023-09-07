from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserCreationForm(UserCreationForm):
        email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"})
    )
         
        class Meta(UserCreationForm.Meta):
            model = User
            fields = ("username", "email")

from django import forms

class TagForm(forms.Form):
    TAG_CHOICES = (
        ('1', 'Бюджетные'),
        ('2', 'Дорогие'),
        ('3', 'Рабочие'),
        ('4', 'Бюджетные видеокарты'),
    )
    tag = forms.ChoiceField(choices=TAG_CHOICES, widget=forms.RadioSelect)

