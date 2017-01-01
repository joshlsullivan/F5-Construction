from django.shortcuts import render
import requests
from django.views import View

class JobsView(View):
    def get(self, request):
        url = "https://api.servicem8.com/api_1.0/Job.json"
        r = requests.get(url, auth=('robert@f5.construction', 'TB@1Robert'))
        jobs = r.json()
        return render(request, 'jobs/index.html', {'jobs': jobs})
