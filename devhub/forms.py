from django import forms
from .models import Project, DevJournal

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'status', 'tech_stack', 'github_url']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'tech_stack': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Django, Postgres, React'}),
            'github_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://github.com/...'}),
        }

class DevJournalForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter project choices to only the current user's projects
        self.fields['project'].queryset = Project.objects.filter(user=user)

    class Meta:
        model = DevJournal
        fields = ['date', 'title', 'project', 'content']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entry Title'}),
            'project': forms.Select(attrs={'class': 'form-select'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'What did you build or learn today?'}),
        }
