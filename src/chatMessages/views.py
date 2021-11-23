from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from .models import Message
from django.http import JsonResponse
import ast


class SendMessage(APIView):

    def post(self, request):
        body = ast.literal_eval(request.body.decode("utf-8"))
        x = Message.objects.create(owner=request.user, text=body['text'])
        x.save()
        return JsonResponse({"status": 'ok'})


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
