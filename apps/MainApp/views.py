from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages

def index (request):
    return render(request,'MainApp/index.html')

def createUser (request):
    return render(request, 'MainApp/createUser.html')

def Add(request):
    errors = User.objects.basic_validator(request.POST)
    if len(messages):
        for tag, error in messages.iteritems():
            messages.error(request, error, extra_tags=tag)
            return redirect('/createUser',messages )
    if request.POST['Password'] != request.POST['ConfirmPassword']:
        return render(request,'MainApp/register.html',messages)
    else:
        return render(request, 'MainApp/index.html', {"User": User.objects.get(Email=request.POST['Email'])})

def FriendPage (request):
    loggedUser = User.objects.get(id=request.session['userId'])
    context = {'logged_in_user' : loggedUser}
    return render(request, 'MainApp/FriendPage.html',{"User": User.objects.all()}, context)

def Login(request):
    if request.method == 'POST':
        message = User.objects.Login_validation(request.POST)
    if message['status']:
        user = message['user']
        request.session['logOn'] = 'True'
        request.session['userId'] = user.id
        print user.id
        return redirect('/')
    else:
        messages.error = "invalid username/password"
        return redirect('/')

def Logout(request):
    request.session.clear()
    return redirect('/')

def AddFriend(request,User_id):
    with_user = User.objects.get(id=User_id)
    loggedUser = User.objects.get(id=request.session['userId'])
    loggedUser.Friendships.add(with_user)
    return redirect('/FriendPage',loggedUser)

def UnFriend(request,User_id):
    with_user = User.objects.get(id=User_id)
    loggedUser = User.objects.get(id=request.session['userId'])
    loggedUser.Friendships.remove(with_user)
    return redirect('/FriendPage')