from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Notification
from .seriallizers import NotificationSerializer
from django.views.decorators.http import require_http_methods
import json
from .helpers import Helpers
from .utils.processing import Processing


# Create your views here.
@require_http_methods(["GET", "POST"])
def all_notifications(request):
    if request.method == "GET":
        try:
            notifications = list(Notification.objects.all().values())  # all data from the Notification table
            processing_data = Processing(data=notifications, params=request.GET)
            formatted_data = processing_data.process_data()
            return Helpers.success_response(formatted_data['data'], warnings=formatted_data['warnings'])
        except KeyError as e:
            return Helpers.internal_server_error(f"This field does not exist in the Notification table: {str(e)}",
                                                 status=400)
        except Exception as e:
            return Helpers.internal_server_error(str(e))

    elif request.method == "POST":
        data = json.loads(request.body)
        notification = Notification.objects.create(title=data['title'], content=data['content'])
        return Helpers.success_created(notification.__str__())


@require_http_methods(["GET", "PUT", "DELETE"])
def notification_detail(request, pk):
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
        return JsonResponse({"data": None, "meta": {}}, status=500)
