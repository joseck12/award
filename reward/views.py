from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect


# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
  id = request.user.id
  profile = Profile.objects.get(user=id)
