from django.contrib import admin
from .models import Service, Order, Icon, OrderedService
# Register your models here.
admin.site.register(Service)
admin.site.register(Order)
admin.site.register(Icon)
admin.site.register(OrderedService)