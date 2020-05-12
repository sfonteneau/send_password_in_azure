#!/usr/bin/python
import sys 
from azure.common.credentials import UserPassCredentials
from azure.graphrbac import GraphRbacManagementClient
from azure.graphrbac.models import PasswordProfile, UserUpdateParameters
import configparser
import base64

newpassword = base64.b64decode(sys.argv[2]).decode('utf-8')

try:
    mail = sys.argv[1]
except:
    mail = ''

## Get configuration

config = configparser.ConfigParser()
config.read('/etc/azureconf/azure.conf')

mailadmin = config.get('common', 'mailadmin')
passwordadmin = config.get('common', 'passwordadmin')
tenantid = config.get('common', 'tenantid')

def main():

    credentials = UserPassCredentials(
    mailadmin, passwordadmin, resource="https://graph.windows.net"
    )

    graphrbac_client = GraphRbacManagementClient(
       credentials,
       tenantid
    )

    param = UserUpdateParameters(
                    password_profile=PasswordProfile(
                    password=newpassword,
                    force_change_password_next_login=False
                    )
            )

    user = graphrbac_client.users.update(mail, param)

main()
