from .models import Part
from django.db.models import Q


def search_part(request):
    query = ''

    if request.GET.get('query'):
        query = request.GET.get('query')

    parts = Part.objects.distinct().filter(
        Q(catalog_number__icontains=query),
        Q(name__icontains=query),
    )
