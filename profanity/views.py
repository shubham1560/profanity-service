from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from .services import get_profanity_matrix, check_string_profanity, profanity_array
from profanity_service.profanity import profanity_prob


class CheckProfanity(APIView):

    def post(self, request, format=None):
        result = get_profanity_matrix(request)
        return Response(result, status=status.HTTP_200_OK)


class WakeUpCall(APIView):

    def get(self, request, format=None):
        return Response('', status=status.HTTP_200_OK)


class CheckStringForProfanity(APIView):

    def post(self, request, format=None):
        result = check_string_profanity(request)
        return Response(result, status=status.HTTP_200_OK)


class CheckProfanityArray(APIView):

    def post(self, request, format=None):
        result = profanity_array(request.data['array_string'])
        return Response(result, status=status.HTTP_200_OK)