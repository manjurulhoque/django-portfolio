from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('project-details/<slug:slug>', ProjectDetailView.as_view(), name='project-details'),
    path('blog', BlogListView.as_view(), name='blog'),
    path('blog/<slug:slug>', BlogDetailView.as_view(), name='blog-details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)