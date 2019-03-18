from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^search/', views.search,name = 'search'),

]
