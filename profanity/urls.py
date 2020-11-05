from django.urls import path, include
from .views import CheckProfanity, WakeUpCall

urlpatterns = [
    path("check/", CheckProfanity.as_view())
    path("wake/", WakeUpCall.as_view())
]