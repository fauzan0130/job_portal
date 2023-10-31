from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('job/<int:job_id>/apply/', views.apply_job, name='apply_job'),
    path('register/', views.user_registration, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('job_listings/', views.job_listings, name='job_listings'),
    path('create_job_listing/', views.create_job, name='create_job_listing'),
    path('edit_job_listing/<int:job_id>/', views.edit_job, name='edit_job_listing'),
    path('delete_job_listing/<int:job_id>/', views.delete_job, name='delete_job_listing'),
    path('job_applications/<int:job_id>/', views.job_applications, name='job_applications'),
    path('view_user_profile/<str:username>/', views.view_user_profile, name='view_user_profile'),
    path('job/<int:job_id>/', views.job_details, name='job_details'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
