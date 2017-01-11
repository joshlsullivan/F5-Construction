from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests
from requests.auth import HTTPBasicAuth
import json
from django.contrib.auth.decorators import login_required
from .forms import JobSubmissionForm
from jobs.models import JobsSubmitted
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage

@login_required
def submit_job(request):
    if request.method == 'POST':
        form = JobSubmissionForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            job_description = form.cleaned_data['job_description']
            job_address = form.cleaned_data['job_address']
            company = request.user.username
            user = request.user
            url = "https://api.servicem8.com/api_1.0/Job.json"
            payload = {
                "status":"Quote",
                "job_address":job_address,
                "job_description":"{0} {1} {2} {3}".format(first_name, last_name, email, phone, job_description),
                "company_id":company,
            }
            r = requests.post(url, data=payload, auth=(settings.SERVICEM8_EMAIL, settings.SERVICEM8_PASSWORD))
            j = JobsSubmitted(job_id=r.headers['x-record-uuid'], first_name=first_name, last_name=last_name, email=email, phone=phone, job_description=job_description, job_address=job_address, company=company, user=user)
            j.save()
            email = EmailMessage(
                'New Job Submission for {} {}'.format(first_name, last_name),
                job_description,
                'services@f5.construction',
                [user.email,],
                ['tim@f5.construction', 'robert@f5.construction'],
            )
            return HttpResponseRedirect('/jobs')
    else:
        form = JobSubmissionForm()
    return render(request, 'jobsubmissionform/submit.html', {'form':form})
