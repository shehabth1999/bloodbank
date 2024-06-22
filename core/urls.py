"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from hospital.views import index, SearchBlood, about, contact, reaserches, DonateBlood

urlpatterns = [
    path('', index, name='home'),
    path('blood/search/', SearchBlood.as_view(), name='get_blood'),
    path('blood/donate/', DonateBlood.as_view(), name='donate_blood'),
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('hospital/', include('hospital.urls')),

    path('about-us/', about, name='about-us'),
    path('contact-us/', contact, name='contact-us'),
    path('reaserches/', reaserches, name='reaserches'),
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)