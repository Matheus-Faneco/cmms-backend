from django.shortcuts import render
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.decorators import api_view
from machines.models import Machine

@api_view(['GET'])
def cached_machine_list(request):
    data = cache.get('machine_list')

    if data is None:
        data = list(Machine.objects.values())
        cache.set('machine_list', data, timeout=60)

    return Response(data)

