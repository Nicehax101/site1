from mysite import forms
from django.shortcuts import redirect, render,get_object_or_404
from django.template import RequestContext, context
from django.views.generic import View,ListView,DetailView
from django.http import HttpResponseRedirect
from videos.forms import postform
from django.http import HttpResponse
from .models import Video
from . import models
from . import forms

#changed videosview,videos_detailview to class based views

class videosview(ListView,Video):

    template_name='videos/platform.html'
    context_object_name='videos'
    queryset = Video.objects.all().order_by('-date')

class videos_detailview(DetailView):
    model= Video
    template_name= 'videos/videos_detail.html'  
    context_object_name='video'


def new_post(request):
    if request.method == 'POST':
        form = postform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('videos:index')
    else:
        form = postform()
        return render(request, 'videos/newpost.html',{'form':form,})
