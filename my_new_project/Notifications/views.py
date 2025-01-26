from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,JsonResponse
from .seriallizers import NotificationSerializer
from .models import Notification
from django.views.decorators.http import require_http_methods
import json

@require_http_methods(["GET", "POST"])
def all_notifications(request):
    print("Request method: " , request.method)
    if request.method == "GET":
        notifications = Notification.objects.all()
        return JsonResponse({
            "data": list(notifications.values()),
            "success": True,
            "meta": {
                "total": len(notifications),
            }
        },status=200)
    elif request.method == "POST":
        data = json.loads(request.body)
        notification = Notification.objects.create(title=data["title"],content=data["content"])
        return JsonResponse({"data": notification.__str__(),"meta": {},
                             "success": True },status=201)


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