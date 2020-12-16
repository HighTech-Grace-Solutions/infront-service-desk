from django import forms
from django.forms.widgets import Select, SelectMultiple


class SelectWOA(Select):
    """
    Select With Option Attributes:
        subclass of Django's Select widget that allows attributes in options, 
        like disabled="disabled", title="help text", class="some classes",
              style="background: color;"...

    Pass a dict instead of a string for its label:
        choices = [ ('value_1', 'label_1'),
                    ...
                    ('value_k', {'label': 'label_k', 'foo': 'bar', ...}),
                    ... ]
    The option k will be rendered as:
        <option value="value_k" foo="bar" ...>label_k</option>
    """

    def create_option(self, name, value, label, selected, index,
                      subindex=None, attrs=None):
        if isinstance(label, dict):
            opt_attrs = label.copy()
            label = opt_attrs.pop('label')
        else:
            opt_attrs = {}
        option_dict = super(SelectWOA, self).create_option(name, value,
                                                           label, selected, index, subindex=subindex, attrs=attrs)
        for key, val in opt_attrs.items():
            option_dict['attrs'][key] = val
        return option_dict


SUPPORT_GROUP = [
    ('', {'label': 'Not set', 'style': 'display: none'}),
    ('Support Group 1', {
     'label': 'Support Group 1', 'type': 'Support Group 1'}),
    ('Support Group 2', {
     'label': 'Support Group 2', 'type': 'Support Group 2'}),
    ('Support Group 3', {
     'label': 'Support Group 3', 'type': 'Support Group 3'}),
]


class SupportGroupForm(forms.Form):
    inputSupportGroup = forms.ChoiceField(
        label="Colors",
        choices=SUPPORT_GROUP,
        widget=SelectWOA(attrs={
            'id': 'inputSupportGroup',
            'class': 'selectpicker form-control',
            'data-live-search': 'true'
        }))

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)