from django.urls import path, re_path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('api/neighbors/', views.NeighborhoodList.as_view(), name='neighbor'),
    path('api/neighbors/update/<int:pk>/', views.NeighborhoodList.as_view(), name='neighbor_update'),
    path('api/neighbors/delete/<int:pk>/', views.NeighborhoodList.as_view(), name='neighbor_delete'),
    path('api/users/', views.UserList.as_view(), name='users'),
    path('api/users/update/<int:pk>/', views.UserList.as_view(), name='users_update'),
    path('api/users/delete/<int:pk>/', views.UserList.as_view(), name='users_delete'),
    path('api/business/', views.BusinessList.as_view(), name='business'),
    path('api/business/update/<int:pk>/', views.BusinessList.as_view(), name='business_update'),
    path('api/business/delete/<int:pk>/', views.BusinessList.as_view(), name='business_delete'),
]
