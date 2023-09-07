from django.urls import path, include,re_path
from . import views
from django.urls import include 
from users.views import Register
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('django.contrib.auth.urls')),

    path('register/', Register.as_view(), name = 'register'),
    re_path(r'^$', views.Catalog.product_list, name='product_list'),
    re_path(r'^(?P<category_slug>[-\w]+)/$',
        views.Catalog.product_list,
        name='product_list_by_category'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.Catalog.product_detail,
        name='product_detail'),
    
]





