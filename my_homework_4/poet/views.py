
from random import random
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Poet

@api_view(["GET", "POST"])
def all_poets(request):
    if request.method == "GET":
        poets = list(Poet.objects.all().values())
        return Response({"poets": poets,
                         })

    elif request.method == "POST":
        poet = Poet.objects.create(
            name = request.data["name"],
            genre = request.data["genre"],
            poetry = request.data["poetry"],
        )
        return Response({
            "id": poet.id,
            "name": poet.name,
            "genre": poet.genre,
            "poetry" : poet.poetry

        },status=status.HTTP_200_OK)


@api_view(["GET"])  # Разрешаем только GET-запросы
def random_poem(request):
    try:
        poems = list(Poet.objects.values_list("poetry", flat=True))
        print(poems)

        if not poems:
            return Response({"error": "No poems found"}, status=404)

        random_poems = random.choice(poems)
        return Response({"poem": random_poems})

    except Exception as e:
        return Response({"error": str(e)}, status=500)  # Показываем ошибку


@api_view(["DELETE"])
def delete_poem(request,pk):
    poem = get_object_or_404(Poet, pk=pk)
    poem.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)