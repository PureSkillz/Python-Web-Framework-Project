from django import forms

from gameshop.common.helpers import BootstrapFormMixin
from gameshop.main.models import Game, Periphery


class CreateGameForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        # commit false does not persist to database
        # just returns the object to be created
        game = super().save(commit=False)

        game.user = self.user
        if commit:
            game.save()

        return game

    class Meta:
        model = Game
        fields = [field.name for field in model._meta.fields if field.name != "user"]
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter game name',
                }
            ),
        }


class CreatePeripheryForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        # commit false does not persist to database
        # just returns the object to be created
        periphery = super().save(commit=False)

        periphery.user = self.user
        if commit:
            periphery.save()

        return periphery

    class Meta:
        model = Periphery
        fields = [field.name for field in model._meta.fields if field.name != "user"]
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter periphery name',
                }
            ),
            'date_of_release': forms.DateInput(format=["%d-%m-%Y"], )
        }