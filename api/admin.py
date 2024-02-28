from django.contrib import admin

from .models import room, students, Ip, Route, RouteThrough, Shops

# Register your models here.


admin.site.register(room)
admin.site.register(students)

admin.site.register(Ip)
admin.site.register(Route)
admin.site.register(RouteThrough)
admin.site.register(Shops)


