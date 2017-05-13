from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

# Create your views here.
def index(request):
    user = request.user
    if user.is_authenticated():
        user = request.user
        return render(
            request,
            'index.html',
            context={
                'user': user
            }
        )
    else:
        return redirect('login')
def boards(request):
    return render(
        request,
        'boards.html',
        context={

        }
    )

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
