"""
    ~ views for your `jobs` application
"""
from django.shortcuts import render

# Create your views here.
def home(request):
    """
    View for your Home/Index page
    """
    return render(request, 'jobs/home.html')
