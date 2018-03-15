from django.urls import path
from django.views.generic import TemplateView

from .views import OpenDoorView


urlpatterns = [
    path('open/', OpenDoorView.as_view(), name='open_door'),
    path('', TemplateView.as_view(template_name='door/open_button.html'), name='open_button'),
]
