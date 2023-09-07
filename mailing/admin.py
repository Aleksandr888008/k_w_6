from django.contrib import admin

from mailing.models import Client, Message, SetMessage, LogMessage


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'is_active')
    search_fields = ('last_name',)
    list_filter = ('first_name', 'last_name', 'is_active')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name', 'is_publication')


@admin.register(SetMessage)
class SetMessageAdmin(admin.ModelAdmin):
    list_display = ('time', 'frequency', 'status')
    list_filter = ('time',)
    search_fields = ('status',)
    