from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('api/user/', views.UserList.as_view(), name='user-list'),
    path('api/get-user/', views.GetUser.as_view(), name='get-user'),
    path('api/user/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('api/form/', views.FormSubmissionList.as_view(), name='formsubmission-list'),
    path('api/form/<int:pk>/', views.FormSubmissionDetail.as_view(), name='formsubmission-detail'),
    path('api/city/', views.CityList.as_view(), name='city-list'),
    path('api/city/<int:pk>/', views.CityDetail.as_view(), name='city-detail'),
    path('api/location/', views.LocationList.as_view(), name='location-list'),
    path('api/location/<int:pk>/', views.LocationDetail.as_view(), name='location-detail'),
    path('api/group/', views.GroupList.as_view(), name='group-list'),
    path('api/group/<int:pk>/', views.GroupDetail.as_view(), name='group-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)