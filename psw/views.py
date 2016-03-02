"""
Definition of views.
"""
import paramiko

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from psw.forms import pswCreateForm, CommandForm, pswAuthenticationForm, ServicesForm
from subprocess import call
from psw.models import Commands, Services
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django import forms

def ip_adding():
    ip_tuple = Commands.objects.values_list('ip')
    ip_list = [x[0] for x in ip_tuple]
    ip_start = ['192.168.0.','10']
    ip_join = ip_start[0] + ip_start[1]
    

    for item in ip_list:
        if item == ip_join:
            a = int(ip_start[1])+1
            ip_start[1] = str(a)
            ip_join = ip_start[0] + ip_start[1]
            
        else:
            ip_join
    return ip_join
        
        


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'psw/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'psw/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'psw/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )

def register(request):
    if request.method == 'POST':
        form = pswCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('poszło')
    form = pswCreateForm()
    return render(request, 'psw/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
            else:
                return HttpResponse('Nie poszło - nieaktywny')
        else:
            return HttpResponse('Nie poszło - złe dane')
    return render(request, 'psw/login.html', {'form': pswAuthenticationForm(request.POST)})

def servers(request):
    if request.method == 'POST':
        form = CommandForm(request.POST)
        
        if form.is_valid():
            form.instance.user = request.user
            ip = ip_adding()
            form.instance.ip = ip
            name = form.cleaned_data['name']
            #ip = form.cleaned_data['ip']
            system = form.cleaned_data['system']
            ram = form.cleaned_data['ram']
            quote = form.cleaned_data['quote']
            username = str(request.user.get_username())
            #commandlog = 'python3.5 /root/log_skrypt.py'+ ' '+ ip + ' ' + system + ' ' + ram + ' ' + quote +  ' ' + username + name + ' >> PSW_log.log'
            #command = 'python3.5 /root/main_skrypt.py'+ ' '+ ip + ' ' + system + ' ' + ram + ' ' + quote + ' ' + username + name +'  > wyniki_testy.txt'
            form.save()

            #Tworzenie ze skryptu.py Python 3.5 
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect('89.206.7.46', username='root', password='TrudneHaslo123')
                # Tworzenie Log
                #stdin, stdout, stderr = ssh.exec_command(commandlog)
                # Tworzenie kontenerow
                #stdin, stdout, stderr = ssh.exec_command(command)
                ssh.close()
            except paramiko.ssh_exception.NoValidConnectionsError as e:
                print ('Error %s' %e)
                return HttpResponseRedirect('servers/')
            return HttpResponseRedirect('/')
    else:
         form = CommandForm()
    return render(request, 'psw/servers.html', {'form': form})

def listservers(request):
    
    servers = Commands.objects.filter(user=request.user)
    context_dict = {'servers': servers}
    return render(request, 'psw/listservers.html' , context_dict)

def services(request):
    
    if request.method == 'POST':
        qs = Commands.objects.filter(user=request.user)
        form = ServicesForm(request.POST,user=request.user)
        
        if form.is_valid():
            
            sql = form.cleaned_data['sql']
            http = form.cleaned_data['http']
            php = form.cleaned_data['php']
            form.save()
            return HttpResponseRedirect('services/')
            
    else:
        form = ServicesForm()
    return render(request, 'psw/services.html', {'form': form})

