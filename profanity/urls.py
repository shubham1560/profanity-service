from django.urls import path, include
from .views import CheckProfanity

urlpatterns = [
    path("check/", CheckProfanity.as_view())
]