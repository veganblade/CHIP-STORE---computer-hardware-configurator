from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


from django.urls import path

from users.views import configurate
from django.urls import path
from users import views
from django.urls import path
from users.views import configurate, my_builds



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    
    path('profile/', TemplateView.as_view(template_name='profile.html'), name='profile'),
    
    path('favorites/', TemplateView.as_view(template_name='favorites.html'), name='favorites'),
    path('users/', include('users.urls'), name='users'),
    path('configurate/', configurate, name='configurate'),
    path('my_builds/', my_builds, name='my_builds'),
    path('assembly/', TemplateView.as_view(template_name='assembly.html'), name='assembly'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
