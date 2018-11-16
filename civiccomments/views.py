from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
import settings
import requests
from models import *
def homepage(request):
    return render(request, 'homepage.html', {})

def aboutpage(request):
    return render(request, 'about.html', {})

def create_issue(request):
    return render(request, 'create_issue.html', {})


def api_create_issue(request):
    new_issue =Issue(title=request.POST['title'], description=request.POST['description'])
    new_issue.save()
    return JsonResponse({}, safe=False)

def view_issue(request, uuid):
    issue = Issue.objects.get(uuid=uuid)
    return render(request, 'view_issue.html', {'title': issue.title, 'description': issue.description})

def create_comment(request):
    return JsonResponse({}, safe=False)
