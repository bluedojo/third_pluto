from django.urls import path
from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('api/v1/items', views.dietary_item_collection),
]

urlpatterns = format_suffix_patterns(urlpatterns)
