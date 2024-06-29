"""Models for the `jobs` application"""
from django.db import models

# Create your models here.
class Job(models.Model):
    '''Model is just a Python class that can be saved into a database.'''
    # image property ---> Images
    image = models.ImageField(upload_to='images/')
    # summary property -> Summary
    summary = models.CharField(max_length=200)
