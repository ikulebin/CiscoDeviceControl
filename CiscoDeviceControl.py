from netmiko import ConnectHandler
import netmiko
from pprint import pprint
from paramiko.ssh_exception import AuthenticationException


cisco_router = {'device_type': 'cisco_ios',# 'cisco_s300'предопределенный тип устройства
                    'ip': ip,  # адрес устройства
                    'username': '',  # имя пользователя
                    'password': '',  # пароль пользователя
                    'secret': '',  # пароль режима enable
                    'port': 22,  # порт SSH, по умолчанию 22
                    }
    try:
        ssh = ConnectHandler(**cisco_router)