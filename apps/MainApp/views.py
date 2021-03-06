from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages

def index (request):
    return render(request,'MainApp/index.html')

def createUser (request):
    return render(request, 'MainApp/createUser.html')

def Add(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
            return redirect('/createUser',messages )
    if request.POST['Password'] != request.POST['ConfirmPassword']:
        return render(request,'MainApp/register.html',messages)
    else:
        return render(request, 'MainApp/index.html', {"User": User.objects.get(Email=request.POST['Email'])})

def FriendPage (request):
    if 'logOn' not in request.session:
        return redirect('/')
    else:
        loggedUser = User.objects.get(id=request.session['userId'])
        context = {'logged_in_user' : loggedUser, 'all_users' : User.objects.all}
        return render(request, 'MainApp/FriendPage.html', context=context)

def Organizerpage (request):
    if 'logOn' not in request.session:
        return redirect('/')
    else:
        loggedUser = User.objects.get(id=request.session['userId']) 
        Is_organizer = User(id = loggedUser).Isorganizer      
        context = {
            'loggedUser' : loggedUser,
            'Is_organizer' : Is_organizer 
        }
        Is_organizer = User(id = loggedUser).Isorganizer
        return render(request, 'MainApp/Organizerpage.html', context=context)

def organizerregastration (request):
    if 'logOn' not in request.session:
        return redirect('/')
    else:    
        loggedUser = User.objects.get(id=request.session['userId'])
        context = {
            'loggedUser' : loggedUser,
            'User' : User.objects.all
        }
        return render(request, 'MainApp/organizerregastration.html', context=context)

def addorganizer (request):
    loggedUser = User.objects.get(id=request.session['userId'])  
    errors = User.objects.Organizer_validation(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
            return redirect('/organizerregastration',messages )
    else:
        return render(request, 'MainApp/index.html', {"User": User.objects.get(Email=request.POST['Email'])})

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