from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from base.models import Message, Room, Topic, User, Prediction


class CustomUserAdmin(UserAdmin):
    """User model admin."""
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'created', 'modified')


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'host', 'description')
    search_fields = ('name', 'host__username')
    list_filter = ('topic',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('body', 'user', 'room')    
    search_fields = ('user__username', 'room__name')
    list_filter = ('user', 'room')


@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = ('result', 'country', 'instrument', 'decade', 'mood', 'topic', 'date')


admin.site.register(User, CustomUserAdmin)
admin.site.register(Topic)
