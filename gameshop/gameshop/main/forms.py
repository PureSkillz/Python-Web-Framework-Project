from django import forms
from django.urls import reverse_lazy

from gameshop.common.helpers import BootstrapFormMixin, DisabledFieldsFormMixin
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
        exclude = ('user',)
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter game name',
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'placeholder': 'Enter game price',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter game description (optional)',
                }
            ),
            'developer': forms.TextInput(
                attrs={
                    'placeholder': 'Enter game developer (optional)',
                }
            ),
        }


class EditGameForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Game
        exclude = ('user',)


class DeleteGameForm(BootstrapFormMixin, DisabledFieldsFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_disabled_fields()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Game
        exclude = ('user',)


# --------------------------------------------------------------------------


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
        exclude = ('user',)
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter periphery name',
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'placeholder': 'Enter periphery price',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter periphery description (optional)',
                }
            ),
            'warranty': forms.TextInput(
                attrs={
                    'placeholder': 'Enter periphery warranty in months (optional)',
                }
            ),
        }


class EditPeripheryForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Periphery
        exclude = ('user',)


class DeletePeripheryForm(BootstrapFormMixin, DisabledFieldsFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_disabled_fields()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Periphery
        exclude = ('user',)
