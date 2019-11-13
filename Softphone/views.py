from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.hashers import check_password, make_password


##############################################FUNCTIONS##################################################
#Home
def index(request):
    return render(request, "login.html", {})

########################################Authentication Views######################################
#Login
@csrf_exempt
def loginUser(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            role = request.POST['role']
            print(username,password,role)
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    print('here')
                    if(role=='admin'):
                        print('user role is admin')
                        if user.is_superuser:
                            print('user checked is admin')
                            login(request, user)
                            return JsonResponse({'status':'success','message':'user login successfull'})
                        else:
                            return JsonResponse({'status':'error','message':'No such admin account found '})
                    else:
                        print('user role is agent')
                        if user.is_superuser == False:
                            login(request, user)
                            return JsonResponse({'status':'success','message':'user login successfull'})
                        else:
                            return JsonResponse({'status':'error','message':'Please choose correct role '})
                else:
                    return JsonResponse({'status':'error','message':'user account is disabled'})
            else:
                return JsonResponse({'status':'error','message':'Invalid credentials'})
    except Exception as e:
        print('error',e) 



#Logout
@csrf_exempt
def logoutUser(request):
    logout(request)
    return redirect('/') 

###################################################################################################


##########################################ADMIN URLS###############################################
#Admin Dashboard
@login_required(login_url='/')
def adminDashboard(request):
    return render(request, "admin_dashboard.html", {})

#Create Account
@login_required(login_url='/')
def createClientAccount(request):
    return render(request, "create_client.html", {})


#Create New Agent
@csrf_exempt
@login_required(login_url='/')
def createNewAgent(request):
    if(request.method=='GET'):
        return render(request, "create_agent.html", {})
    else:
        try:
            if request.method == 'POST':
                print('>>>>>.',request.POST)
                f_name = request.POST['f_name']
                l_name = request.POST['l_name']
                email = request.POST['email']
                phone = request.POST['phone']
                password = request.POST['password']
                enc_password = make_password(password)
                role = request.POST['role']
                try:
                    agent_exists = User.objects.get(email = email)
                    if agent_exists:
                        return JsonResponse({'status':'error','message':'Agent with same email already exists'})
                except Exception as e:
                    pass
                user_data = User.objects.create(first_name=f_name, last_name=l_name, email=email, 
                    password=enc_password, username=email)
                user_data.save()
                user = User.objects.get(email = email)
                agent_data = Agents.objects.create(user_ref=user, role=role, phone_number=phone)
                agent_data.save()
                return JsonResponse({'status':'success','message':'Agent created successfully'})
        except Exception as e:
            print('error in createAgent',e)

###################################################################################################

##########################################AGENT URLS###############################################
#Agent Dashboard
@login_required(login_url='/')
def agentDashboard(request):
    return render(request, "agent_dashboard.html", {})


