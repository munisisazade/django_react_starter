from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
	# Example api
	path('example/', views.ApiExample.as_view(), name='example-api'),
    
    # path('country/', views.CountryApi.as_view(), name="country-api"),
]
