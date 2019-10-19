"""digital_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.apps import apps
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from machina import urls as machina_urls
# from apps.app import application
# from paypal.payflow.dashboard.app import application as payflow
# from paypal.express.dashboard.app import application as express_dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include(apps.get_app_config('oscar').urls[0])),
    # path('oauth/', include('social_django.urls', namespace='social')),
    path('checkout/paypal/', include('paypal.express.urls')),
    # path('dashboard/paypal/payflow/', payflow.urls),
    # Dashboard views for Express
    # path('dashboard/paypal/express/', express_dashboard.urls),
    # path('', application.urls),
    path('forum/', include(machina_urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
