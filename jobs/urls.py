from django.conf.urls import url

from . import views

app_name = 'jobs'
urlpatterns = [
    url(r'^$', views.get_jobs, name='jobs-list'),
    url(r'^(?P<jobssubmitted_id>[0-9]+)/$', views.get_job_detail, name='detail'),
    url(r'^(?P<jobssubmitted_id>[0-9]+)/note/$', views.get_job_note, name='note'),
    #url(r'^(?P<jobssubmitted_id>[0-9]+)/attachment/$', views.get_job_attachment, name='attachment'),
]
