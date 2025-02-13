import random
from django.http import JsonResponse
from django.views import View



class PredictView(View):
    def get(self, request):

        predictions = [
            "Вас чекає удача!",
            "Сьогодні чудовий день для нових починань.",
            "Будьте обережні, попереду перешкоди.",
            "Вас очікує зустріч з цікавою людиною.",
            "Ваші зусилля скоро дадуть плоди.",
            "Сьогодні варто прислухатися до своєї інтуїції.",
            "Будьте готові до несподіваних сюрпризів.",
            "Успіх супроводжуватиме ваші починання.",
            "Настає час змін.",
            "Скоро ви отримаєте хороші новини."
        ]


        random_prediction = random.choice(predictions)


        return JsonResponse({
            "prediction": random_prediction
        })

