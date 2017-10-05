from django import forms

class TxtForm(forms.Form):
    txt = forms.TextField(
        label="txt",
        required=True,
    )

class NumForm(forms.Form):
    num = forms.NumField(
        label="num",
        required=True,
        max_length=2,
    )
