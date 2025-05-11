from django.urls import path, include


urlpatterns = [
    path('deals/', include('api.deals.urls')),
]