from django.contrib import admin
from .models import Project, DevJournal

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'status', 'tech_stack', 'updated_at')
    list_filter = ('status', 'user')
    search_fields = ('title', 'description', 'tech_stack')
    ordering = ('-updated_at',)

@admin.register(DevJournal)
class DevJournalAdmin(admin.ModelAdmin):
    list_display = ('date', 'title', 'project', 'user', 'created_at')
    list_filter = ('date', 'project', 'user')
    search_fields = ('title', 'content')
    ordering = ('-date', '-created_at')
