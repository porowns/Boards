from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .utils import getGroup
# Create your views here.
def index(request):
    user = request.user
    if user.is_authenticated():
        user = request.user
        usergroup = getGroup(user)
        return render(
            request,
            'index.html',
            context={
                'user': user,
                'usergroup': usergroup,
            }
        )
    else:
        return redirect('login')
def boards(request):
    user = request.user
    if user.is_authenticated():
        user = request.user
        usergroup = getGroup(user)
        return render(
            request,
            'boards.html',
            context={
                'user': user,
                'usergroup': usergroup,
            }
        )
    else:
        return redirect('login')

def profile(request):
    return render(
        request,
        'profile.html',
        context={

        }
    )

def register(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if not username or not password:
        print "hi"
        return render(
            request,
            'register.html',
            context={

            }
        )
    else:
        print "else"

        user = User(username=username)
        user.set_password(password)
        user.save()
        user = authenticate(username = username, password=password)
        user_group = Group.objects.get(name="User")
        user_group.user_set.add(user)
        login(request, user)
        return redirect('/')

def loginUser(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request,user)
            return redirect('/')
        else:
            return redirect('/gay')

    else:
        return render(
            request,
            'login.html',
            context={

            }
        )

def logoutUser(request):
    logout(request)
    return redirect('/login')
