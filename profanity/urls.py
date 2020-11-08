from django.urls import path, include
from .views import CheckProfanity, WakeUpCall, CheckStringForProfanity, CheckProfanityArray

urlpatterns = [
    path("check/", CheckProfanity.as_view()),
    path("wake/", WakeUpCall.as_view()),
    path('check_string/', CheckStringForProfanity.as_view()),
    path('check_string_array/', CheckProfanityArray.as_view())

]