from django.db import models
from django.contrib.auth.models import User

class ProjectStatus(models.TextChoices):
    IDEA = 'idea', 'Idea'
    BUILDING = 'building', 'Building'
    DONE = 'done', 'Done'

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=10,
        choices=ProjectStatus.choices,
        default=ProjectStatus.IDEA
    )
    tech_stack = models.CharField(
        max_length=255,
        help_text="Comma-separated tags, e.g., Python, Django, PostgreSQL, Bootstrap"
    )
    github_url = models.URLField(blank=True, null=True, verbose_name="GitHub Repository URL")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return self.title

    def get_tech_stack_list(self):
        if self.tech_stack:
            return [tag.strip() for tag in self.tech_stack.split(',')]
        return []


class DevJournal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='journal_entries')
    project = models.ForeignKey(
        Project,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='journal_entries',
        help_text="Optional: Link this note directly to a project."
    )
    date = models.DateField()
    title = models.CharField(max_length=200)
    content = models.TextField(help_text="What did you build, fix, or learn today?")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', '-created_at']

    def __str__(self):
        return f"{self.date} - {self.title}"
