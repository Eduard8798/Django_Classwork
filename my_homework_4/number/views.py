import random

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def rundom_numbers_many(request, pk):
    rundom_number = random.randint(1, pk)
    return JsonResponse({"rundom_number": rundom_number,
                         "range": f"1-{pk}"})


@require_http_methods(["GET"])
def rundom_numer_one(request):
    rundom_number = random.randint(1, 100)
    return JsonResponse({"rundom_number": rundom_number, })


@require_http_methods(["GET"])
def rundom_numbers_diapazone(request, pk, pd):
    if (pk > pd):
        rundom_number = random.randint(pd, pk)
        return JsonResponse({"rundom_number": rundom_number,
                             "range": f"{pd}-{pk}"})
