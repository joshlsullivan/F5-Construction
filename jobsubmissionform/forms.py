from django import forms

PROPERTY_MANAGEMENT_COMPANY = (
    ('personal', 'Personal'),
    ('twelverivers', 'Twelve Rivers'),
)

class JobSubmissionForm(forms.Form):
    name = forms.CharField(label="Name", max_length=140)
    email = forms.EmailField(label="Email")
    phone = forms.CharField(label="Phone", max_length=20)
    job_description = forms.CharField(label="Job description", widget=forms.Textarea)
    job_address = forms.CharField(label="Job address", widget=forms.Textarea)
#    company = forms.ChoiceField(
#        required=True,
#        widget=forms.Select,
#        choices=PROPERTY_MANAGEMENT_COMPANY,
#    )
