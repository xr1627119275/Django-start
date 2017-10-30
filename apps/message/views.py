# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import UserMessage
# Create your views here.
def getform(request):
    message = None
    all_message = UserMessage.objects.get(name='bobby2')
    if all_message:
        message = all_message
    return render(request, 'form_message.html', {'my_message': message})