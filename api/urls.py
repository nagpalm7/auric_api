from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('api/user/', views.UserList.as_view(), name='user-list'),
    path('api/user/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('api/form/', views.FormSubmissionList.as_view(), name='formsubmission-list'),
    path('api/form/<int:pk>/', views.FormSubmissionDetail.as_view(), name='formsubmission-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)