from django.conf.urls import url

from MarketApp import views

urlpatterns = [
    url('^market/',views.market,name='market'),
]