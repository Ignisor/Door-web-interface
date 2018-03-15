from django.urls import path

from .views import OpenDoorView


urlpatterns = [
    path('open/', OpenDoorView.as_view(), name='open_door'),
]
