#coding=utf-8
from django.shortcuts import render
from blog.models import BlogsPost
from django.shortcuts import render_to_response
from django.http import HttpResponse,Http404
import datetime


# Create your views here.
def index(request):
    blog_list = BlogsPost.objects.all()
    return render_to_response('index.html', {'blog_list': blog_list})

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s. </body></html>" % now
    return HttpResponse(html)

def hours_ahead(request,offset):

    try:
        offset  = int(offset)
    except ValueError:
        raise
    dt = datetime.datetime.now()+datetime.timedelta(hours=offset)
    #assert False
    html = "<html><body>In %s hour(s),it well be %s</body></html>" %(offset,dt)
    return HttpResponse(html)