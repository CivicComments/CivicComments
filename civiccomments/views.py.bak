from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
import settings
import requests
from models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

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
    return render(request, 'view_issue.html', {'title': issue.title, 'description': issue.description, 'uuid': uuid, 'comments': Comment.objects.filter(issue=issue)})

def view_issues(request):
    issues = Issue.objects.all()
    paginator = Paginator(issues, 25) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        paginated_issues = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paginated_issues = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        paginated_issues = paginator.page(paginator.num_pages)
    return render(request, 'issues.html', {'issues': paginated_issues})



def create_comment(request):
    issue = Issue.objects.get(uuid=request.POST['issue_uuid'])
    new_comment = Comment(issue=issue, authored_by=request.user, content=request.POST['comment'])
    new_comment.save()
    return JsonResponse({}, safe=False)
