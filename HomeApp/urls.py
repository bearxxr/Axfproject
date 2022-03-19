from django.conf.urls import url

from HomeApp import views

urlpatterns = [
    url(r'^test/',views.test,name='test'),
    url(r'^home/',views.home,name='home'),
]