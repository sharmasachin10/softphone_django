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


#Clients View
@login_required(login_url='/')
def clients(request):
    return render(request, "clients_view.html", {})


#Agents View
@login_required(login_url='/')
def agents(request):
    agents_list = []
    agents_dict = {'id':'','first_name':'','last_name':'','email':'', 'role':'', 'phone':'', 'date_joined':''}
    agents_data = Agents.objects.all()
    for agent in agents_data:
        print('agent',agent.user_ref.first_name)
        agents_dict['id']=agent.id
        agents_dict['role']=agent.role
        agents_dict['phone']=agent.phone_number
        agents_dict['first_name']=agent.user_ref.first_name
        agents_dict['last_name']=agent.user_ref.last_name
        agents_dict['email']=agent.user_ref.email
        agents_dict['date_joined']=agent.user_ref.date_joined
        agents_list.append(agents_dict.copy())
    return render(request, "agents_view.html", {'agents':agents_list})


#Delete Agent
@login_required(login_url='/')
def deleteAgent(request,agent_id):
    try:
        print('here in delete',agent_id)
        agent_data = Agents.objects.filter(id=str(agent_id))
        for data in agent_data:
            user_id = data.user_ref.id
            user_instance = User.objects.get(id=user_id)
        agent_data.delete()
        user_instance.delete()
        return redirect('/agents/')
    except Exception as e:
        print('error in deleteAgent',e)

#Create Account
@csrf_exempt
@login_required(login_url='/')
def createClientAccount(request):
    if(request.method=='GET'):
        return render(request, "create_client.html", {})
    else:
        try:
            if request.method == 'POST':
                print('>>>>>.',request.POST)
                #Customer Details
                client_name = request.POST.get('client_name')
                client_id = request.POST.get('client_id')
                switch_id = request.POST.get('switch_id')
                client_exists = Clients.objects.get(client_id=client_id)
                if client_exists:
                    return JsonResponse({'status':'error','message':'Client with same client id already exists'})
                else:
                    client_data = Clients.objects.create(client_name=client_name, client_id=client_id,
                        switch_id=switch_id)
                    client_data.save()

                client_info = Clients.objects.get(client_id=client_id)

        except Exception as e:
            print('error in createClientAccount')


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


