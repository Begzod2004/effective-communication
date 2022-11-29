from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.contact.api.v1.urls'))
]
