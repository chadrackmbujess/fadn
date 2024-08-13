from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def signup(request):
    
    if request.method=="POST":
        get_email=request.POST.get('name')
        get_password=request.POST.get('pass1')
        get_confirm_password=request.POST.get('pass2')
        if get_password!=get_confirm_password:
            messages.info(request,"Le mot de passe n'est pas correspondant" )
            return redirect('/auth/signup/')
        
        try:
            if User.objects.get(username=get_email):
                messages.warning(request,"nom est pris")
                return redirect('/auth/signup/')
        except Exception as identifier:
            pass
        myuser=User.objects.create_user(get_email,get_email,get_password)
        myuser.save()

        myuser= authenticate(username=get_email,password=get_password)

        if myuser is not None:

            login(request,myuser)
            messages.success(request,"Utilisateur est enregistré")
            return redirect('/')

        
    return render(request,'signup.html')

def handleLogin(request):
    if request.method=="POST":
        get_email=request.POST.get('name')
        get_password=request.POST.get('pass1')
        myuser= authenticate(username=get_email,password=get_password)

        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Connexion Succès")
            return redirect('/')
        else:
            messages.error(request,"Informations d'identification non valides")
    return render(request,'login.html')

def handleLogout(request):
    logout(request)
    messages.success(request,'Déconnexion avec succès')
    return render(request,'login.html')