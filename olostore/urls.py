"""
URL configuration for olostore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from store.views import product_list, add_to_cart, view_cart, checkout, homepage, product_detail, detail, addpanier

urlpatterns = [
    path('', product_list, name='product-list'),
    path('add_to_cart/<int:pk>/', add_to_cart, name='add-to-cart'),
    path('view_cart/', view_cart, name='view-cart'),
    path('checkout/', checkout, name='checkout'),
    path('admin/', admin.site.urls),
    #path('tev/', include('store.urls')),
    #path('', homepage, name='home'),
    #path('product/<int:pk>/', product_detail, name='product_detail'),
   # path('product/', detail, name='detail'),
    path('product/<int:product_id>/', detail, name='detail'),
    path('panier/', addpanier, name='addpanier'),
    

]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)