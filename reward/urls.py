from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^search/', views.search,name = 'search'),
    url(r'^new/project$',views.newproject, name='newproject'),
    url(r'^profile/(\d+)', views.profile, name='profile'),

]
