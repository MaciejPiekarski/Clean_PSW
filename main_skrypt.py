# -*- coding: utf-8 -*-
import sys
import subprocess
from subprocess import PIPE, call
import time
ip = sys.argv[1]
system = sys.argv[2]
ram = sys.argv[3]
quote = sys.argv[4]

user = sys.argv[5]
'''system = 'Ubuntu'
ram = '128'
quote = '2'''

def low_letters(*argsl):
    user = argsl[0].lower() 
    system = argsl[1].lower()

    return user, system

def creating_id():

    all_id = []
    command = "vzlist | awk '{print $1}'"
    uid = 1
    
    proc = subprocess.Popen(command, shell=True, stdout=PIPE, universal_newlines=True)

    for line in iter(proc.stdout.readline, ''):
        all_id.append(line.rstrip('\n'))

    all_id = [int(i) for i in all_id[1:]]
    
    for item in all_id:
        if item == uid: 
            uid = uid + 1
            
        else :
            uid 
    return uid       

def creating_name(*argsn):
    server_name = str(argsn[0]) + '_' + argsn[1] + '_' + argsn[2] + '_' + argsn[3]
    host_name = argsn[0] + str(creating_id()) + '.test.pl'
    return server_name, host_name

def choose_system(*argss):
    system = ''

    if 'ubuntu' in argss[0]:
        system = 'ubuntu-12.04-x86_64'
    elif 'debian' in argss[0]:
        system = 'debian'
    else:
        system = 'inny'
    return system
    
    


def creating_contener(*argsc):
    uid = str(creating_id())
    server_name = creating_name(low[0],low[1],ram,quote)

    com_create = 'vzctl create ' + uid + ' --ostemplate ' + choose_system(low[1]) + ' --config vswap-1g'
    com_name = 'vzctl set ' + uid + ' --save --name ' + uid + '_' + server_name[0]
    com_boot = 'vzctl set ' + uid + ' --save --onboot yes'
    com_host = 'vzctl set ' + uid + ' --save --hostname ' + server_name[1]
    com_netif = 'vzctl set ' + uid + ' --save --netif_add eth0,,,1C:75:08:25:7A:02'
    com_domain = 'vzctl set ' + uid + ' --save --searchdomain test.pl'
    com_nameserver = 'vzctl set ' + uid + ' --save --nameserver 8.8.8.8 --nameserver 8.8.4.4'
    com_cpu = 'vzctl set ' + uid + ' --save --cpus 2'
    com_ram = 'vzctl set ' + uid + ' --save --ram ' + argsc[2] + 'M'
    com_quote = 'vzctl set ' + uid + ' --save --diskspace ' + argsc[3] + 'G'
    com_start = 'vzctl start ' + uid 

#--------------------------------------
    proc_create = subprocess.call(com_create, shell=True, stdout=PIPE, universal_newlines=True)
    proc_create
        
#--------------------------------------
    proc_name = subprocess.call(com_name, shell=True, stdout=PIPE, universal_newlines=True)
    proc_name
#--------------------------------------
    proc_boot = subprocess.call(com_boot, shell=True, stdout=PIPE, universal_newlines=True)
    proc_boot
#--------------------------------------
    proc_host = subprocess.call(com_host, shell=True, stdout=PIPE, universal_newlines=True)
    proc_host    
#--------------------------------------
    proc_netif = subprocess.call(com_netif, shell=True, stdout=PIPE, universal_newlines=True)
    proc_netif
#--------------------------------------    
    proc_domain = subprocess.call(com_domain, shell=True, stdout=PIPE, universal_newlines=True)
    proc_domain
#--------------------------------------
    proc_nameserver = subprocess.call(com_nameserver, shell=True, stdout=PIPE, universal_newlines=True)
    proc_nameserver
#--------------------------------------
    proc_cpu = subprocess.call(com_cpu, shell=True, stdout=PIPE, universal_newlines=True)
    proc_cpu
#--------------------------------------
    proc_ram = subprocess.call(com_ram, shell=True, stdout=PIPE, universal_newlines=True)
    proc_ram
#--------------------------------------
    proc_quote = subprocess.call(com_quote, shell=True, stdout=PIPE, universal_newlines=True)
    proc_quote
#--------------------------------------
    proc_start = subprocess.call(com_start, shell=True, stdout=PIPE, universal_newlines=True)
    proc_start
    
    return com_create, com_name, com_boot, com_host, com_ram, com_quote 
 





low = low_letters(user,system)
server_id = creating_id()
server_name = creating_name(low[0],low[1],ram,quote)
chsystem = choose_system(low[1])
con = creating_contener(user,system,ram,quote)
'''print ('ID: ', server_id)
print ('Server name: ', server_name[0])
print ('Host name: ', server_name[1])
print ('System:',chsystem)
print ('contener create:',con[0])
print ('contener name:',con[1])
print ('contener boot:',con[2])
print ('contener host:',con[3])
print ('contener ram:',con[4])
print ('contener quote:',con[5])'''


