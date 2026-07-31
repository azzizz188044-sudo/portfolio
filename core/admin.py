from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "project_date",
    )

    search_fields = (
        "title",
    )

    list_filter = (
        "project_date",
    )