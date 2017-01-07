from django.contrib import admin
from jobs.models import JobsSubmitted
# Register your models here.
class JobsSubmittedAdmin(admin.ModelAdmin):
    fields = ('job_id', 'name', 'job_address', 'job_description', 'user', 'company')
    list_display = ('job_id', 'name', 'job_address', 'job_description', 'user', 'company')

admin.site.register(JobsSubmitted, JobsSubmittedAdmin)
