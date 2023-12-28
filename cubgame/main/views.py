from django.shortcuts import render

def index(request):
  data={
    'title': 'Главная страница',
    'values': ['Some', 'Hello', '123'],
    "user": request.user,
    "is_auth_user": False if request.user.username == "" else True
  }
  return render(request,'main/index.html', data)

def about(request):
  data = {
    "user": request.user,
    "is_auth_user": False if request.user.username == "" else True
  }
  return render(request,'main/about.html', data)


def link(request):
  data = {
    "user": request.user,
    "is_auth_user": False if request.user.username == "" else True
  }
  return render(request, 'main/link.html', data)