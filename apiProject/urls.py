from django.urls import path

from .views import ProfileList, ProfileDetails, profile_list_view

urlpatterns = [
    path('api/profile/', ProfileList, name='add_profile'),
    path('api/view-profile/<int:id>', ProfileDetails, name='edit_profile'),
    path('', profile_list_view, name='profile_list')
]