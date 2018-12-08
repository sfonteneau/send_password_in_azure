#!/usr/bin/python
import sys 
from azure.common.credentials import UserPassCredentials
from azure.graphrbac import GraphRbacManagementClient
from azure.graphrbac.models import PasswordProfile, UserUpdateParameters
from ConfigParser import SafeConfigParser

login = sys.argv[1]
newpassword = sys.argv[2].decode('base64')
try:
    mail = sys.argv[3]
except:
    mail = ''

## Get confgiruation
config = SafeConfigParser()
config.read('azure.conf')

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
