from django import forms
from aldryn_accordion.models import Accordion

class AccordionPluginForm(forms.ModelForm):
    class Meta:
        model = Accordion
        exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')
