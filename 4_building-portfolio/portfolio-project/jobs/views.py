"""
    ~ views for your `jobs` application
"""
from django.shortcuts import render
from .models import Job

# Create your views here.
def home(request):
    """
    View for your Home/Index page
    """
    # jobs = Job.objects
    # or like this
    jobs = Job.objects.all()
    return render(request, 'jobs/home.html', {'jobs': jobs})
