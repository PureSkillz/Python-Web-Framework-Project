from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from gameshop.accounts.models import Profile
from gameshop.common.helpers import BootstrapFormMixin, DisabledFieldsFormMixin


class CreateProfileForm(BootstrapFormMixin, auth_forms.UserCreationForm):
    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_LENGTH,
    )
    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LENGTH,
    )
    picture = forms.ImageField(required=False)
    date_of_birth = forms.DateField(required=False)
    description = forms.CharField(
        widget=forms.Textarea,
        required=False
    )
    email = forms.EmailField(

    )
    gender = forms.ChoiceField(
        choices=Profile.GENDERS,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            picture=self.cleaned_data['picture'],
            date_of_birth=self.cleaned_data['date_of_birth'],
            description=self.cleaned_data['description'],
            email=self.cleaned_data['email'],
            gender=self.cleaned_data['gender'],
            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'picture', 'description', 'date_of_birth')
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Enter first name',
        #         }
        #     ),
        #     'last_name': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Enter last name',
        #         }
        #     ),
        #     'email': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Enter your email',
        #         }
        #     ),
        #     'date_of_birth': forms.DateInput(
        #         attrs={
        #             'placeholder': 'yyyy-mm-dd',
        #         }
        #     ),
        # }


class EditProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Profile
        exclude = ('user',)

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name',
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'placeholder': 'yyyy-mm-dd',
                }
            ),
        }


class DeleteProfileForm(BootstrapFormMixin, DisabledFieldsFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_disabled_fields()

    def save(self, commit=True):
        self.instance.user.delete()
        return self.instance

    class Meta:
        model = Profile
        exclude = ('user',)
