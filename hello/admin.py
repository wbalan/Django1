from django.contrib import admin

# Register your models here.
from hello.models import Car, Card, RouteSheet
admin.site.register(Car)
admin.site.register(Card)
admin.site.register(RouteSheet)

