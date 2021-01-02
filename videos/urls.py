from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import (
    videosview,
    videos_detailview,
    
) 


app_name = 'videos'
urlpatterns = [
    path('', videosview.as_view(), name='index'),
    path('create',views.new_post, name='newpost'),
    path('video/<slug>',videos_detailview.as_view(),name='detail'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)