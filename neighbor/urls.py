from django.urls import path, re_path
from django.conf import settings
from . import views
from django.conf.urls.static import static

import neighbor

urlpatterns = [
    # user
    path('api/users/', views.UserDetailList.as_view(), name='users'),
    path('api/users/update/<int:pk>/', views.UserList.as_view(), name='users_update'),
    path('api/users/delete/<int:pk>/', views.UserList.as_view(), name='users_delete'),
    path('api/users/get/<int:pk>/', views.UserList.as_view(), name='users_get'),
    path('api/users/search/<name>/', views.UserSearchList.as_view(), name='users_search'),
  
    # neighbor
    path('api/neighbors/', views.NeighborhoodDetailList.as_view(), name='neighbor'),
    path('api/neighbors/update/<int:pk>/', views.NeighborhoodList.as_view(), name='neighbor_update'),
    path('api/neighbors/delete/<int:pk>/', views.NeighborhoodList.as_view(), name='neighbor_delete'),
    path('api/neighbors/get/<int:pk>/', views.NeighborhoodList.as_view(), name='neighbor_get'),
    path('api/neighbors/search/<name>',views.NeighborhoodSearchList.as_view(), name='neighbor_search'),

    # business    
    path('api/business/', views.BusinessDetailList.as_view(), name='business'),
    path('api/business/update/<int:pk>/', views.BusinessList.as_view(), name='business_update'),
    path('api/business/delete/<int:pk>/', views.BusinessList.as_view(), name='business_delete'),
    path('api/business/get/<int:pk>/', views.BusinessList.as_view(), name='business_get'),
    path('api/business/search/<name>',views.BusinessSearchList.as_view(), name='business_search'),

]
