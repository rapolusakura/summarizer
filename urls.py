# howdy/urls.py
from django.conf.urls import url
from howdy import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='main'),
    url(r'^results/', views.Done, name='results'),
    url(r'^about/', views.About, name='about')
]
