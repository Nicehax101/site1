from mysite import forms
from django.shortcuts import redirect, render,get_object_or_404
from django.urls import reverse
from django.template import RequestContext, context
from django.views.generic import View,ListView,DetailView,CreateView,DeleteView,UpdateView
from django.http import HttpResponseRedirect
from videos.forms import postform
from django.http import HttpResponse
from .models import Video
from django.utils import timezone
from . import models
from . import forms
import datetime


#changed videosview,videos_detailview to class based views

class videosview(ListView,Video):

    template_name='videos/platform.html'
    context_object_name='videos'
    queryset = Video.objects.all().order_by('-date')

class videos_detailview(DetailView):
    model= Video
    template_name= 'videos/videos_detail.html'  
    context_object_name='video'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['updated'] = datetime.datetime.now()
        return context

class VideoCreateView(CreateView):
    model = Video
    template_name = "videos/newpost.html"
    form_class = postform

    def form_valid(self, form) :
        form.save()
        return redirect(reverse("videos:detail", kwargs={
            'slug': form.instance.slug}))



class VideoUpdateView(UpdateView):
    model = Video
    template_name = "videos/update.html"
    form_class = postform
    context_object_name = 'video'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['updated'] = datetime.datetime.now()
        return context
    


    def form_valid(self, form) :
        

        form.save()

        return redirect(reverse("videos:detail", kwargs={
            'slug': form.instance.slug}))

    