from django import forms

from gameshop.common.helpers import BootstrapFormMixin, DisabledFieldsFormMixin
from gameshop.main.models import Game, Periphery


class CreateFormMixin(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        # commit false does not persist to database
        # just returns the object to be created
        obj = super().save(commit=False)

        obj.user = self.user
        if commit:
            obj.save()

        return obj


class EditFormMixin(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()


class DeleteForm(BootstrapFormMixin, DisabledFieldsFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_disabled_fields()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

# Game ------------------------------------------------------------


class CreateGameForm(CreateFormMixin):
    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)

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


class EditGameForm(EditFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta(CreateGameForm.Meta):
        pass


class DeleteGameForm(DeleteForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Game
        exclude = ('user',)


# Periphery --------------------------------------------------------------------------


class CreatePeripheryForm(CreateFormMixin):
    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)

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


class EditPeripheryForm(EditFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta(CreatePeripheryForm.Meta):
        pass


class DeletePeripheryForm(DeleteForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Periphery
        exclude = ('user',)
