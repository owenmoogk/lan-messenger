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