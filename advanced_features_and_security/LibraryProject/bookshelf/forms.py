from django import forms

class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, strip=True)

class ExampleForm(forms.Form):
    example_field = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter example text'}),
    )