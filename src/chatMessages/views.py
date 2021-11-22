from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from .forms import MessageForm
from .models import Message

# Create your views here.
@login_required
def homeView(request):

    if request.method == "POST" and "send" in request.POST:
        form = MessageForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.owner = request.user
            event.save()
        return(HttpResponseRedirect("/home"))

    items = Message.objects.all()
    addForm = MessageForm()

    context = {
        "items": items,
        "addForm": addForm,
    }
    return render(request, "home.html", context)

from django.http import JsonResponse


def getMessages(request):

    messages = Message.objects.all()

    messageData = []

    for message in messages:
        messageData.append({
            "owner": message.owner.username,
            "text": message.text
        })
    return JsonResponse({
        'user': request.user.username,
        'items': messageData
    })