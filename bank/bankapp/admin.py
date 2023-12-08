from django.contrib import admin

from bankapp.models import District, Account, Branchs, Material

# Register your models here.
admin.site.register(District)
admin.site.register(Branchs)
admin.site.register(Account)
admin.site.register(Material)