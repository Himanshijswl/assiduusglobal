from django.db import models


class Employee(models.Model):
    full_name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    employment_status = models.CharField(max_length=50)
    sub_unit = models.CharField(max_length=50)