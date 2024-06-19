from django import forms


class JsonRpcForm(forms.Form):
    method = forms.CharField(max_length=100, label='Method')
    params = forms.CharField(widget=forms.Textarea, label='Params')
