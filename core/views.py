from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import *


def home(request):
    about = {}
    for a in About.objects.all():
        about[a.key] = a.value

    context = {
        'about': about,
        'services': Service.objects.all(),
        'experiences': Experience.objects.all(),
        'projects': Project.objects.all().select_related('project_category'),
        'categories': ProjectCategory.objects.all(),
        'skills': Skill.objects.all(),
        'educations': Education.objects.all(),
        'blogs': Blog.objects.all().select_related('category')
    }
    return render(request, 'home.html', context)


class ProjectDetailView(DetailView):
    model = Project
    template_name = "project-details.html"
    slug_url_kwarg = "slug"
    slug_field = "slug"
    context_object_name = 'project'


class BlogListView(ListView):
    template_name = "blogs.html"
    paginate_by = 10
    context_object_name = "blogs"
    queryset = Blog.objects.select_related('category').order_by('id')


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog-details.html"
    slug_url_kwarg = "slug"
    slug_field = "slug"
    context_object_name = "blog"
