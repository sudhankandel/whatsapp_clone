from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views import View
from django.contrib.auth import get_user_model
from django.shortcuts import Http404
from chats.models import Thread, Message

User = get_user_model()


def index(request):
    users = User.objects.exclude(username=request.user.username)
    return render(request, 'index.html', context={'users': users})

class chatPage(View):
    template_name = 'main_chat.html'

    def get_queryset(self):
        return Thread.objects.by_user(self.request.user)

    def get_object(self):
        other_username  = self.kwargs.get("id")
        self.other_user = get_user_model().objects.get(id=other_username)
        obj = Thread.objects.get_or_create_thread(self.request.user, self.other_user)
        if obj == None:
            raise Http404
        return obj

    def get_context_data(self, **kwargs):
        context = {}
        context['user'] = get_user_model().objects.get(id=self.kwargs.get("id"))
        context['users'] = User.objects.exclude(id=self.request.user.id)
        context['messages'] = self.get_object().message_set.all()   
        return context

    def get(self, request, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context=context)

    def post(self, request, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context=context)


# def chatPage(request, username):
#     me=User.objects.get(id=request.user.id)
#     other_user = User.objects.get(id=username)
#     users = User.objects.exclude(id=request.user.id)
#     obj = Thread.objects.get_or_create_thread(me, other_user)


#     if request.user.id > user_obj.id:
#         thread_name = f'chat_{request.user.id}-{user_obj.id}'
#     else:
#         thread_name = f'chat_{user_obj.id}-{request.user.id}'
#     message_objs = ChatModel.objects.filter(thread_name=thread_name)
#     print(message_objs)
#     return render(request, 'main_chat.html', context={'user': other_user, 'users': users, 'messages': "message_objs"})
