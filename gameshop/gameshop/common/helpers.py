from django import forms


class BootstrapFormMixin:
    fields = {}

    def _init_bootstrap_form_controls(self):
        for _, field in self.fields.items():
            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})
            # if 'class' not in field.widget.attrs:
            #     field.widget.attrs['class'] = ''
            # field.widget.attrs['class'] += ' form-control'


class DisabledFieldsFormMixin:
    disabled_fields = '__all__'
    fields = {}

    def _init_disabled_fields(self):
        del self.fields['image']
        for name, field in self.fields.items():
            field.required = False

            if self.disabled_fields != '__all__' and name not in self.disabled_fields:
                continue

            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})
            if not isinstance(field, forms.ChoiceField):
                field.widget.attrs['readonly'] = 'readonly'
            else:
                field.widget.attrs['disabled'] = 'disabled'