"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Base Api url prefix
    path('api/v1/', include("api.urls", "api")),
]

# Swagger UI documentation Automatic generated
schema_view = get_schema_view(
    openapi.Info(
        title="Example API documentation",
        default_version='0.1.3',
        description="Api documentation created by Munis"
    ),
    public=True,
)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

urlpatterns += [
	# React app
    re_path(r'^.*$', views.ReactView.as_view(), name='react-app'),
]

# in development django built-in server serves static and media content
if not settings.PROD:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# This is change default admin panel Headers and titles
admin.site.site_header = 'Cassandra System Admin'
admin.site.site_title = 'Cassandra System Administration'
admin.site.index_title = 'Cassandra System Administration'
