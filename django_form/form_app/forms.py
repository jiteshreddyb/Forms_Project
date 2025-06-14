from django import forms

class FeedbackForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=100)
    last_name = forms.CharField(label="Last Name", max_length=100)
    email = forms.EmailField(label="Email")
    mobile_no=forms.IntegerField(label="Phone") 
    message = forms.CharField(label="Message", widget=forms.Textarea)