from django.contrib import admin

# mihir123-user@123

# Register your models here.
from .models import Room, Topic, Message

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)

