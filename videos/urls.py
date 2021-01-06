from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import (
    videosview,
    videos_detailview,
    VideoCreateView,
    VideoUpdateView,
    VideoDeleteView,
    
) 


app_name = 'videos'
urlpatterns = [
    path('', videosview.as_view(), name='index'),
    path('create',VideoCreateView.as_view(), name='newpost'),
    path('<slug>',videos_detailview.as_view(),name='detail'),
    path('<slug>/update',VideoUpdateView.as_view(),name='update'),
    path('<slug>/delete',VideoDeleteView.as_view(),name='delete'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)