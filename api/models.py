from django.db import models
import uuid

# Create your models here.


class Shops(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=50)
    
    
class room(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_name = models.CharField(max_length=50)


class students(models.Model):
    std_id = models.AutoField(primary_key=True)

    std_room = models.ForeignKey(room,on_delete=models.CASCADE,related_name="students_set")
    std_name = models.CharField(max_length=50)
    age = models.IntegerField()

class room_teachers(models.Model):
    teacher_name = models.CharField(max_length=50)
    teacher_age = models.CharField(blank=True, null=True)
    teacher_room = models.ForeignKey(room, on_delete=models.CASCADE, related_name="teacher_set")


class Ip(models.Model):
    ip_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)


class Route(models.Model):
    route_name = models.CharField(max_length=50)
    ips = models.ManyToManyField("api.Ip", through="RouteThrough")

class RouteThrough(models.Model):
    ip = models.ForeignKey(Ip, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
         ordering=['-created_at']

    

class Url(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=300)
    remark = models.CharField(max_length=500, null=True, blank=True)
    is_trusted = models.BooleanField(default=False)
    redirects = models.JSONField(null=True, blank=True)
    request_urls = models.JSONField(null=True, blank=True)
    redirects_updated = models.BooleanField(default=False)
    screenshot_updated = models.BooleanField(default=False)
    num = models.IntegerField(null=True, blank=True)

    is_blacklisted_by_tcil = models.BooleanField(default=None, null=True, blank=True)
    is_blacklisted_by_operator = models.BooleanField(
        default=None, null=True, blank=True
    )
    