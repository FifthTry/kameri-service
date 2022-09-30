import django
import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def add_todo(req: django.http.HttpRequest):
    # It should be only POST request
    # Get data from request body and add it to database
    # It will redirect to today's todo page

    if req.method != "POST":
        return django.http.HttpResponse("Wrong Method", status=405)

    body = json.loads(req.body.decode("utf-8"))
    print(body)

    return django.http.JsonResponse({
        "id": "<todo id>",
    })

"""
curl -X POST \
--data '{"title": "Take update from Interns"}' \
http://127.0.0.1:8001/api/add-todo/
"""


@csrf_exempt
def list_todo(req: django.http.HttpRequest):

    if req.method != "GET":
        return django.http.HttpResponse("Wrong Method", status=405)

    return django.http.JsonResponse({
        "data": [
            {
                "id": "<todo id>",
                "title": "<todo title>",
                "status": "<todo status>"
            }
        ],
        "success": True,
        "message": "Todo fetched successfully"
    })

"""
curl -X GET http://127.0.0.1:8001/api/todos/
"""
