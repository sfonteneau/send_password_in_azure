Installation
========================

For use with : https://github.com/sfonteneau/samba4-sync-password

For send password to azure AD


Test
=====
 - pip3 install azure-graphrbac
 - git clone https://github.com/sfonteneau/send_password_in_azure.git
 - mv send_password_in_azure /opt/sync-azure
 - mkdir /etc/azureconf/
 - cd /opt/sync-azure
 - cp -f azure.conf /etc/azureconf/
 - Configure /etc/azureconf/azure.conf

You can try like this:

python /opt/sync-azure/send_password_azure.py username@exemple.com cGFzc3dvcmQ=\n
