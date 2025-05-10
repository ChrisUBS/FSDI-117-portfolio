from django.shortcuts import render
from .models import project, timelineEntry

# Create your views here.
def ProjectsListPageView(request):
    projects = project.objects.all().order_by('-year')
    
    return render(request, 'portfolio/projects_list.html', {"projects": projects})

def ExperienceAndEducationPageView(request):
    timeline = timelineEntry.objects.all().order_by('-from_date')
    
    return render(request, 'portfolio/exp_edu_section.html', {"timeline": timeline})