from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"placeholder": "Name"}))
    # email = forms.EmailField(widget=forms.TextInput(attrs={'type': 'email'}))
    email = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"type": "email", "placeholder": "Email"}))
    # message = forms.Textarea()
    message = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Message"}))