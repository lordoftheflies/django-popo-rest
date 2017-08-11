from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from users import views

urlpatterns = [
    url(r'^foo/$', views.PopoFooList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)