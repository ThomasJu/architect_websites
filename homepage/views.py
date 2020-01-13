from django.shortcuts import render
# Create your views here.
from .models import Employee, Case, Image

def index(request):
    """View function for home page of site."""
    
    context = {
        'employees': Employee.objects.annotate(),
        'cases': Case.objects.annotate(),
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)