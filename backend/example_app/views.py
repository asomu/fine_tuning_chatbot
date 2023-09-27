from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


@api_view(['GET'])
def hello_rest_api(request):
    data = { 'message': 'Hello, Rest API!'}
    return Response(data)