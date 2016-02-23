"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from psw.forms import pswCreateForm, CommandForm, pswAuthenticationForm
import paramiko
from subprocess import call
from psw.models import Commands
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

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
            ip = form.cleaned_data['ip']
            system = form.cleaned_data['system']
            ram = form.cleaned_data['ram']
            quote = form.cleaned_data['quote']
<<<<<<< HEAD
            commandlog = 'python3.5 /root/log_skrypt.py'+ ' '+ ip + ' ' + system + ' ' + ram + ' ' + quote + ' >> psw_log.log'
            command = 'python3.5 /root/main_skrypt.py'+ ' '+ ip + ' ' + system + ' ' + ram + ' ' + quote + '  > wyniki_testy.txt'            
            #form.save()
=======
            username = str(request.user.get_username())
            user_id = request.user.id
            commandlog = 'python3.5 /root/log_skrypt.py'+ ' '+ ip + ' ' + system + ' ' + ram + ' ' + quote +  ' ' + username + ' >> PSW_log.log'
            command = 'python3.5 /root/main_skrypt.py'+ ' '+ ip + ' ' + system + ' ' + ram + ' ' + quote + ' ' + username + '  > wyniki_testy.txt'            
            form.save()
>>>>>>> refs/remotes/origin/pr/1
            #Tworzenie ze skryptu.py Python 3.5 
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect('89.206.7.46', username='root', password='TrudneHaslo123')
                # Tworzenie Log
                stdin, stdout, stderr = ssh.exec_command(commandlog)
                # Tworzenie kontenerow
                stdin, stdout, stderr = ssh.exec_command(command)
                ssh.close()
            except paramiko.ssh_exception.NoValidConnectionsError as e:
                print ('Error %s' %e)
                return HttpResponseRedirect('servers/')
            return HttpResponseRedirect('/')
    else:
         form = CommandForm()
    return render(request, 'psw/servers.html', {'form': form})

def listservers(request):
    servers = Commands.objects.all
    context_dict = {'servers': servers}
    return render(request, 'psw/listservers.html' , context_dict)
