from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
  id = request.user.id
  profile = Profile.objects.get(user=id)


  return render(request, 'index.html',{'profile':profile})


@login_required(login_url='/accounts/login/')
def myprojects(request):
  id = request.user.id
  profile = Profile.objects.get(user=id)

  projects = Project.objects.all().order_by('-pub_date')

  return render(request, 'myproject.html',{'projects':projects,'profile':profile})
def convert_dates(dates):

@login_required(login_url='/accounts/login/')
def password(request):
  id = request.user.id
  profile = Profile.objects.get(user=id)


  return render(request, 'password.html',{'profile':profile})

 class ProjectList(APIView):
  def get(self, request, format=None):
    all_projects = Project.objects.all()
    serializers = ProjectSerializer(all_projects, many=True)
    return Response(serializers.data)
