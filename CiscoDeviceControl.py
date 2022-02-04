from netmiko import ConnectHandler
import DeviceCredentials
import netmiko
import glob
from pprint import pprint
from paramiko.ssh_exception import AuthenticationException


def show_command(ip, command):
    pass


def config_snippet(ip, snippet_filename, write=True):
    pass


path = glob.glob('./ConfigSnippets/*')
print('---'*50)
print('Available snippets:')
for item in path:
    print(item.replace('./ConfigSnippets\\',''))
print('---'*50)
snippet = input("Enter snippet name (Press enter to load 'Default' snippet)   :")
if snippet == []:
    snippet = 'Default'
try:
    with open('./ConfigSnippets\\'+snippet, 'r') as file:
        snippet = file.read()
        snippet = snippet.splitlines()
        if snippet == []:
            print('Snippet file is empty...')
        else:
            pprint(snippet)
except FileNotFoundError:
    print("File not found.... Check {} file...".format(snippet))


try:
    with open('IPListDevices', 'r') as file:
        IP = file.read()
        IP = IP.splitlines()
        if IP == []:
            print('IPListDevices file is empty...')
        else:
            pprint(IP)
except FileNotFoundError:
    print("File not found.... Check IPListDevices...")


for ip in IP:
    pass



'''
def show_command(ip, command):
    cisco_router = {'device_type': 'cisco_ios',  # 'cisco_s300'предопределенный тип устройства
                    'ip': ip,  # адрес устройства
                    'username': DeviceCredentials.username,  # имя пользователя
                    'password': DeviceCredentials.password,  # пароль пользователя
                    'secret': DeviceCredentials.enable_password,  # пароль режима enable
                    'port': 22,  # порт SSH, по умолчанию 22
                    }
    pass


def config_snippet(ip, snippet_filename, write = True):
    cisco_router = {'device_type': 'cisco_ios',  # 'cisco_s300'предопределенный тип устройства
                    'ip': ip,  # адрес устройства
                    'username': DeviceCredentials.username,  # имя пользователя
                    'password': DeviceCredentials.password,  # пароль пользователя
                    'secret': DeviceCredentials.enable_password,  # пароль режима enable
                    'port': 22,  # порт SSH, по умолчанию 22
                    }
    try:
        ssh = ConnectHandler(**cisco_router)
    except netmiko.ssh_exception.NetMikoTimeoutException:
        print('Timeout................')
        continue
    except AuthenticationException:
        print('Login filed................')
        continue


for ip in IP:
    cisco_router = {'device_type': 'cisco_ios',# 'cisco_s300'предопределенный тип устройства
                    'ip': ip,  # адрес устройства
                    'username': DeviceCredentials.username,  # имя пользователя
                    'password': DeviceCredentials.password,  # пароль пользователя
                    'secret': DeviceCredentials.enable_password,  # пароль режима enable
                    'port': 22,  # порт SSH, по умолчанию 22
                    }

    try:
        ssh = ConnectHandler(**cisco_router)
'''
