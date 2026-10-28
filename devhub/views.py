from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project, DevJournal, ProjectStatus
from .forms import ProjectForm, DevJournalForm


@login_required
def project_board(request):
    """Pipeline Board grouping user projects into Idea, Building, Done."""
    projects = Project.objects.filter(user=request.user)

    context = {
        'idea_projects': projects.filter(status=ProjectStatus.IDEA),
        'building_projects': projects.filter(status=ProjectStatus.BUILDING),
        'done_projects': projects.filter(status=ProjectStatus.DONE),
    }
    return render(request, 'devhub/project_board.html', context)


@login_required
def journal_list(request):
    """Daily development log timeline view."""
    entries = DevJournal.objects.filter(user=request.user)
    return render(request, 'devhub/journal_list.html', {'entries': entries})


@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('project_board')
    else:
        form = ProjectForm()
    return render(request, 'devhub/forms.html', {'form': form, 'title': 'Add New Project'})


@login_required
def journal_create(request):
    if request.method == 'POST':
        form = DevJournalForm(request.user, request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('journal_list')
    else:
        form = DevJournalForm(request.user)
    return render(request, 'devhub/form.html', {'form': form, 'title': 'Add Daily Journal Entry'})
