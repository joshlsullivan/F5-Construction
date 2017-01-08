from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class JobsSubmitted(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    job_id = models.CharField(max_length=120)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    job_description = models.TextField()
    job_address = models.TextField()
    company = models.CharField(max_length=80)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Job Submitted"
        verbose_name_plural = "Jobs Submitted"

    def __str__(self):
        return self.job_id
