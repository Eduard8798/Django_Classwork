from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .seriallizers import NotificationSerializer
from .models import Notification
from django.views.decorators.http import require_http_methods
import json
from my_new_project.utils.helpers import Helpers




@require_http_methods(["GET", "POST"])
def all_notifications(request):
    if request.method == "GET":
        notifications = list(Notification.objects.all().values())
        return Helpers.success_response(notifications)

    elif request.method == "POST":
        data = json.loads(request.body)
        notifications = Notification.objects.create(title=data["title"],content=data["content"])
        return Helpers.success_response(notifications.__str__())


@require_http_methods(["GET", "PUT", "DELETE"])
def notification_details(request,pk):
    try:
        if request.method == "GET":
            notification = get_object_or_404(Notification, pk=pk)
            return JsonResponse({
                "id": notification.id,
                "data": notification.__str__(),
                "meta": {},
                "success": True}
                , status=200)
        elif request.method == "PUT":
            notification = get_object_or_404(Notification, pk=pk)
            try:
                data = json.loads(request.body)  # Для raw JSON
            except json.JSONDecodeError:
                return JsonResponse({
                    "success": False,
                    "message": "Invalid JSON format"
                }, status=400)

                # Проверяем и обновляем через сериализатор
            serializer = NotificationSerializer(notification, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
            return JsonResponse({
                "id": notification.id,
                "data": notification.__str__(),
                "meta": {},
                "success": True}
                , status=200)
        elif request.method == "DELETE":
            notification = get_object_or_404(Notification, pk=pk)
            notification.delete()
            return JsonResponse({
                "success": True,
                "message": "Notification successfully deleted!"
            }, status=200)
    except Exception as e:
        return JsonResponse({"data": None,"meta":{} },status=500)