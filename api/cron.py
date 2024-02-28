from .models import  Shops

def first_cron():
    Shops.objects.create(name="Rashidddddd")

def second_cron():
    Shops.objects.create(name="Mehrumma")


