from django import forms
from genre.models import FileObject
from mptt.forms import TreeNodeChoiceField


class FileAddForm(forms.Form):
    name = forms.CharField(max_length=75)
    parent = TreeNodeChoiceField(queryset=FileObject.objects.all())