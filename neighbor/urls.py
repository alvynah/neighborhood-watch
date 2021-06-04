from django.urls import path, re_path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('api/neighbors/', views.NeighborhoodList.as_view(), name='neighbor'),
]
