from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.


def getRoute(request):
    routes = [
        "/api/token"
    ]
    return JsonResponse(routes, safe=False)