from django import forms
from django.core.mail import send_mail

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email', max_length=254)
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        send_mail('Website Inquiry from {}'.format(name), message, email, ['josh@magnolia.technology'], fail_silently=False)
