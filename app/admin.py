from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Customer)
admin.site.register(Agent)
admin.site.register(Station)
admin.site.register(Train)
