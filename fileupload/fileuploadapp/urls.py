from django.conf.urls import url
from fileuploadapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^upload$', views.FileUploadView.as_view())
   
]

if settings.DEBUG:
       urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
       urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
