from django.contrib import admin
from .models import *

admin.site.register(ProjectCategory)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(BlogCategory)
admin.site.register(Service)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ["slug"]


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
