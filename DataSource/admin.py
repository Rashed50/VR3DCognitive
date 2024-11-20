from django.contrib import admin
from DataSource.models import VRModel, VRUser, Country


# Register your models here.
admin.site.register(Country)
admin.site.register(VRModel)
admin.site.register(VRUser)