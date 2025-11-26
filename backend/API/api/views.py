from django.shortcuts import render
from django.http import JsonResponse

def api_view(request):
    data = {
        'name': 'NTWALI',
        'age': 24,
        'country': 'RDC'
    }

    return JsonResponse(data)

