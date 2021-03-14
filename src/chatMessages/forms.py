from django import forms
from .models import Message

# form for a new item
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = [
            "text",
        ]