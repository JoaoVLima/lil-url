from django import forms


class IndexForm(forms.Form):
    long = forms.CharField(label='long', max_length=2048)

