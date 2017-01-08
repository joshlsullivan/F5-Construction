from django import forms

PROPERTY_MANAGEMENT_COMPANY = (
    ('personal', 'Personal'),
    ('twelverivers', 'Twelve Rivers'),
)

class JobSubmissionForm(forms.Form):
    first_name = forms.CharField(label="First name", max_length=80)
    last_name = forms.CharField(label="Last name", max_length=80)
    email = forms.EmailField(label="Email")
    phone = forms.CharField(label="Phone", max_length=20)
    job_description = forms.CharField(label="Job description", widget=forms.Textarea)
    job_address = forms.CharField(label="Job address", widget=forms.Textarea)
#    company = forms.ChoiceField(
#        required=True,
#        widget=forms.Select,
#        choices=PROPERTY_MANAGEMENT_COMPANY,
#    )
