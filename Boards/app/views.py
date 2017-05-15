from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .utils import getGroup
from .models import Board, Post, Category
from django.http import HttpResponse

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
    boards = Board.objects.all()
    categories = Category.objects.all()
    if user.is_authenticated():
        user = request.user
        usergroup = getGroup(user)
        return render(
            request,
            'boards.html',
            context={
                'user': user,
                'boards': boards,
                'categories': categories,
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

def viewBoard(request, pk):
    user = request.user
    board = Board.objects.get(pk=pk)
    post_list = Post.objects.filter(board = board)
    user_list = ['1']
    user_count = len(user_list)
    for post in Post.objects.filter(board = board):
        if post.author in user_list:
            pass
        else:
            user_list.append(post.author)
    if user.is_authenticated():
        user = request.user
        usergroup = getGroup(user)
        return render(
            request,
            'view_board.html',
            context={
                'user': user,
                'usergroup': usergroup,
                'board': board,
                'posts': post_list,
                'user_list': user_list,
                'user_count': user_count,
            }
        )
    else:
        return redirect('login')

def createBoard(request):
    user = request.user
    categories = Category.objects.all()
    if user.is_authenticated():
        user = request.user
        usergroup = getGroup(user)
        if request.method == 'POST':
            title = request.POST.get('title')
            category = Category.objects.get(name =request.POST.get('category'))
            moderator = request.user

            new_board = Board(title = title, category = category, moderator = moderator)
            new_board.save()
            return redirect('/boards')

        else:
            pass
            #form = newBoardForm()
        return render(
            request,
            'create_board.html',
            context={
                'user': user,
                'usergroup': usergroup,
                'categories': categories,
            }
        )
    else:
        return redirect('login')

def modifyBoard(request, pk):
    user = request.user
    board = Board.objects.get(pk=pk)
    categories = Category.objects.all()
    if user.is_authenticated():
        user = request.user
        usergroup = getGroup(user)
        if request.method == 'POST':
            title = request.POST.get('title')
            if title == "":
                title = board.title
            category = Category.objects.get(name =request.POST.get('category'))
            moderator = request.user

            new_board = Board(title = title, category = category, moderator = moderator)
            new_board.save()
            board.delete()
            return redirect('/boards')
        else:
            pass

        return render(
            request,
            'modify_board.html',
            context={
                'user': user,
                'usergroup': usergroup,
                'board': board,
                'categories': categories,
            }
        )
    else:
        return redirect('login')

def removeBoard(request, pk):
    user = request.user
    if user.is_authenticated():
        board = Board.objects.get(pk = pk)
        board.delete()
        return redirect('boards')
    else:
        return redirect('login')

def createPost(request):
    user = request.user
    boards = Board.objects.all()
    if user.is_authenticated():
        user = request.user
        usergroup = getGroup(user)
        if request.method == 'POST':
            print "hello"
            title = request.POST.get('title')
            body = request.POST.get('body')
            author = request.user
            board = Board.objects.get(title=request.POST.get('board'))

            new_post = Post(title=title, body=body, author=author, board=board)
            new_post.save()
            return redirect(board.get_absolute_url())

        else:
            pass
            #form = newBoardForm()
        return render(
            request,
            'create_post.html',
            context={
                'user': user,
                'usergroup': usergroup,
                'boards': boards,
            }
        )
    else:
        return redirect('login')

def modifyPost(request, pk):
    user = request.user
    boards = Board.objects.all()
    old_post = Post.objects.get(pk = pk)
    if user.is_authenticated():
        user = request.user
        usergroup = getGroup(user)
        if request.method == 'POST':
            if request.POST.get('title') == "":
                title = old_post.title
            else:
                title = request.POST.get('title')

            if request.POST.get('body') == "":
                body = old_post.body
            else:
                body = request.POST.get('body')
            author = request.user
            board = Board.objects.get(title=request.POST.get('board'))

            new_post = Post(title=title, body=body, author=author, board=board)
            new_post.save()
            old_post.delete()
            return redirect(board.get_absolute_url())
        else:
            pass
            #form = newBoardForm()
        return render(
            request,
            'modify_post.html',
            context={
                'user': user,
                'usergroup': usergroup,
                'boards': boards,
                'old_post': old_post,
            }
        )
    else:
        return redirect('login')

def removePost(request, pk):
    user = request.user
    post = Post.objects.get(pk = pk)
    board = post.board
    if user.is_authenticated():
        post.delete()
        return redirect(board.get_absolute_url())
    else:
        return redirect('login')

def viewPost(request, pk):
    user = request.user
    if user.is_authenticated():
        user = request.user
        usergroup = getGroup(user)
        post = Post.objects.get(pk=pk)
        return render(
            request,
            'view_post.html',
            context={
                'user': user,
                'usergroup': usergroup,
                'post': post,
            }
        )
    else:
        return redirect('login')
