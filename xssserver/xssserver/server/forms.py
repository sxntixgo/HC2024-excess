from django import forms
from django.forms import ModelChoiceField
from .models import TargetServer


class AttemptForm(forms.Form):
    target_server = ModelChoiceField(queryset=TargetServer.objects.all())
    resource_and_query_string = forms.CharField(max_length=1024)