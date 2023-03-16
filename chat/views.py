from django.shortcuts import render,redirect
from . models import Chats
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout as django_logout
import json
# Create your views here.
import random
Bot_reply=list(["Hi!","hello!!","nice to meet u ","Have a good day","What’s up?","How are you?","How can you help me?","can you help me?","What day is it today?","Which languages can you speak?"])

def signup(request):
    if request.method=="POST":
        try:
            email=request.POST["Email"]
            password=request.POST["Password"]
            user_id=User.objects.get(email=email)
            username=user_id.username
            print(email)
            user = authenticate(request,username=username,email=email,password=password)
            print(username)
            if user is not None:
                login(request, user)
                return redirect("/chatbot")
                # return render(request,"chatbot.html",{"Email":email, "Password":password,"username":username})
            else:
                print("User does not exist!")
                return render(request,"login.html",{"Error":"User does not exist!"})
        except:
            print("wrong creditionals")
            return render(request,"login.html",{"Error":"Invalid input try again!"})

    return render(request,"login.html")

def register(request):
    if request.method=="POST":
        try:
            print("register")
            print(request.POST)
            email=request.POST["Email"]
            username=request.POST["username"]
            password_1=request.POST["password1"]
            password_2=request.POST["password2"]
            if( password_1==password_2 ):
                if not (User.objects.filter(username=username).exists() | User.objects.filter(email=email).exists()):
                    User.objects.create_user(username,email, password_1)
                    user = authenticate(username=username,email=email, password = password_1)
                    login(request, user)
                    return redirect("/chatbot")
                else:
                    return render(request,"register.html",{"Error":"Enter different username and password!"})
            else:
                return render(request,"register.html",{"Error":"Enter same password!"})
            
        except:
            return render(request,"register.html",{"Error":"Invalid input try again!"})

    return render(request,"register.html")

def chatbot(request):
    if request.method == "POST":
        try:
            print("chatbot post called here")
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            username=body["Username"]
            text=body["Text"]
            check=body["Check"]
            length=len(Chats.objects.filter(Username=body["Username"]).values())
            count=length+1
            form=Chats(Username=username,Text=text,Text_order=count,Check=(check==1))
            form.save()

            # bot's rely
            item = random.choice(Bot_reply)
            text=item
            check=0
            count=length+2
            form=Chats(Username=body["Username"],Text=text,Text_order=count,Check=(check==1))
            form.save()
            task = Chats.objects.filter(Username=body["Username"]).values()
            # print(task)
            return redirect("/chatbot")
        except:
            return redirect("/chatbot")
    
    task = Chats.objects.filter(Username=request.user).values()
    length=len(Chats.objects.filter(Username=request.user).values())
    # print(task)
    # print("All chats ")
    # print(request)
    
    return render(request,"chatbot.html",{"mymembers":task,"msg_count":length})

def profile(request):
    if request.method == "POST":
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            # print(body["password1"])
            password1=body["password1"]
            password2=body["password2"]
            if password1==password2 :
                user = User.objects.get(username__exact=request.user)
                user.set_password(password1)
                user.save()
                user = authenticate(username=request.user,password = password1)
                login(request, user)
                print("Password Changed")
        except:
            pass
    return render(request,"profile.html")


def logout(request):
    try:
        django_logout(request)
        print("Successful Logout")
    except:
        pass
    return redirect("/")