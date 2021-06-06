from django.urls import path, re_path
from django.conf import settings
from . import views
from django.conf.urls.static import static

import neighbor

urlpatterns = [
    # neighbor
    path('api/neighbors/', views.NeighborhoodDetailList.as_view(), name='neighbor'),
    path('api/neighbors/post/',views.NeighborhoodPostList.as_view(), name ='neighbor_post'),
    path('api/neighbors/update/<int:pk>/', views.NeighborhoodList.as_view(), name='neighbor_update'),
    path('api/neighbors/delete/<int:pk>/', views.NeighborhoodList.as_view(), name='neighbor_delete'),
    path('api/neighbors/get/<int:pk>/', views.NeighborhoodList.as_view(), name='neighbor_get'),
    path('api/neighbors/search/<name>',views.NeighborhoodSearchList.as_view(), name='neighbor_search'),


    # user
    path('api/users/', views.UserDetailList.as_view(), name='users'),
    path('api/users/post/', views.UserPostList.as_view(), name='users_post'),
    path('api/users/delete/<int:pk>/', views.UserList.as_view(), name='users_delete'),
    path('api/users/get/<int:pk>/', views.UserList.as_view(), name='users_get'),

    # profile
    path('api/profile/', views.ProfileDetailsList.as_view(), name='profiles'),
    path('api/profile/update/<int:pk>/', views.ProfileList.as_view(), name='profiles_update'),
    path('api/profiles/get/<int:pk>/', views.ProfileList.as_view(), name='profiles_get'),
    path('api/profiles/search/<search_term>/', views.ProfileSearchList.as_view(), name='profiles_search'),
  
    

    # business    
    path('api/business/', views.BusinessDetailList.as_view(), name='business'),
    path('api/business/post/', views.BusinessPostList.as_view(), name='business_post'),
    path('api/business/update/<int:pk>/', views.BusinessList.as_view(), name='business_update'),
    path('api/business/delete/<int:pk>/', views.BusinessList.as_view(), name='business_delete'),
    path('api/business/get/<int:pk>/', views.BusinessList.as_view(), name='business_get'),
    path('api/business/search/<name>',views.BusinessSearchList.as_view(), name='business_search'),

    # post    
    path('api/posts/', views.PostDetailList.as_view(), name='posts'),
    path('api/posts/post/', views.PostPostList.as_view(), name='posts_post'),
    path('api/posts/update/<int:pk>/', views.PostList.as_view(), name='posts_update'),
    path('api/posts/delete/<int:pk>/', views.PostList.as_view(), name='posts_delete'),
    path('api/posts/get/<int:pk>/', views.PostList.as_view(), name='posts_get'),
    path('api/posts/search/<name>',views.PostSearchList.as_view(), name='posts_search'),

]
