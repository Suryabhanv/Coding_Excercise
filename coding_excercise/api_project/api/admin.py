# api/admin.py

from django.contrib import admin
from .models import Company, Client, ClientUser

admin.site.register(Company)
admin.site.register(Client)
admin.site.register(ClientUser)
