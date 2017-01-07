from django.shortcuts import get_object_or_404, render
import requests
from django.views import View
from .models import JobsSubmitted
from django.contrib.auth.decorators import login_required
from django.conf import settings

@login_required
def get_jobs(request):
    jobs = JobsSubmitted.objects.all()
    return render(request, 'jobs/index.html', {'jobs': jobs})

@login_required
def get_job_detail(request, jobssubmitted_id):
    j = get_object_or_404(JobsSubmitted, pk=jobssubmitted_id)
    url = "https://api.servicem8.com/api_1.0/Job/{}.json".format(j.job_id)
    r = requests.get(url, auth=(settings.SERVICEM8_EMAIL, settings.SERVICEM8_PASSWORD))
    job = r.json()
    return render(request, "jobs/details.html", {'job': job})

@login_required
def get_job_note(request, jobssubmitted_id):
    a = get_object_or_404(JobsSubmitted, pk=jobssubmitted_id)
    url = "https://api.servicem8.com/api_1.0/Note.json"
    r = requests.get(url, auth=(settings.SERVICEM8_EMAIL, settings.SERVICEM8_PASSWORD))
    notes = r.json()
    return render(request, "jobs/notes.html", {'notes': notes, 'a': a})

@login_required
def get_job_attachment(request, jobssubmitted_id):
    a = get_object_or_404(JobsSubmitted, pk=jobssubmitted_id)
    url = "https://api.servicem8.com/api_1.0/Attachment.json"
    r = requests.get(url, auth=(settings.SERVICEM8_EMAIL, settings.SERVICEM8_PASSWORD))
    attachments = r.json()
    return render(request, "jobs/attachments.html", {'attachments': attachments, 'a': a})
