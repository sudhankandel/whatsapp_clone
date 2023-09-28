from django.contrib import admin
from chats.models import ChatModel
from chats.models import Message, Thread


class MessageInline(admin.StackedInline):
    model = Message
    fields = ('sender', 'text')
    readonly_fields = ('sender', 'text')


class ThreadAdmin(admin.ModelAdmin):
    model = Thread
    inlines = (MessageInline,)

admin.site.register(Thread, ThreadAdmin)
# Register your models here.
admin.site.register(ChatModel)
