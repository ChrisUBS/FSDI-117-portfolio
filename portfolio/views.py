from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import project, timelineEntry
from .forms import ProjectForm

# Create your views here.
def ProjectsListPageView(request):
    projects = project.objects.all().order_by('-year')
    return render(request, 'portfolio/projects_list.html', {"projects": projects})

def ExperienceAndEducationPageView(request):
    timeline = timelineEntry.objects.all().order_by('-from_date')
    return render(request, 'portfolio/exp_edu_section.html', {"timeline": timeline})

@login_required
def NewProjectPageView(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects_list')
    else:
        form = ProjectForm()

    return render(request, 'portfolio/new_project.html', {'form': form})
