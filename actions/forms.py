from django.forms import ModelForm, ChoiceField
from django.contrib.auth.models import User
from .models import Action


def get_current_users():
    return [(u.username, u.username) for u in User.objects.all()]


class ActionForm(ModelForm):

    class Meta:
        model = Action
        fields = ['title', 'description', 'user']
        widgets = {
            'name': ChoiceField(choices=get_current_users),
        }
