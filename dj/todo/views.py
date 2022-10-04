import django
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Todo


# Create your views here.


@csrf_exempt
def add_todo(req: django.http.HttpRequest):
    # It should be only POST request
    # Get data from request body and add it to database
    # It will redirect to today's todo page

    if req.method != "POST":
        return django.http.HttpResponse("Wrong Method", status=405)

    body = json.loads(req.body.decode("utf-8"))

    # Todo.objects.create(
    #     title=body["title"], status=body["status"], description=body["description"]
    # )

    print("TODO Added: ", body)
    return django.http.JsonResponse(
        {
            "data": {
                "kameri-app/add-todo/#title-error": "title is mandatory",
                "kameri-app/add-todo/#status-error": "status is mandatory",
                "kameri-app/add-todo/#description-error": "description is mandatory",
            }
        },
        status=200,
    )

    # return django.http.JsonResponse({"data": {"url": "/"}}, status=200)


"""
curl -X POST \
--data '{"title": "Take update from Interns"}' \
http://127.0.0.1:8001/api/add-todo/
"""


@csrf_exempt
def list_todo(req: django.http.HttpRequest):

    if req.method != "GET":
        return django.http.HttpResponse("Wrong Method", status=405)

    mapper = lambda x: {
        "title": x.title,
        "status": x.status,
        "description": x.description,
    }

    return django.http.JsonResponse(
        list(map(mapper, Todo.objects.all())),
        safe=False,
    )


"""
curl -X GET http://127.0.0.1:8001/api/todos/
"""


@csrf_exempt
def update_todo(req: django.http.HttpRequest):

    if req.method != "POST":
        return django.http.HttpResponse("Wrong Method", status=405)

    body = json.loads(req.body.decode("utf-8"))
    status = body.get("status")
    if not status:
        # Return error fields
        return django.http.JsonResponse(
            {
                "success": False,
                "error": {"todo#status": "Status is mandatory field"},
                "message": "missing mandatory fields",
            },
            status=200,
        )

    print(body, status)

    return django.http.JsonResponse(
        {
            "data": [
                {"id": "<todo id>", "title": "<todo title>", "status": "<todo status>"}
            ],
            "success": True,
            "message": "updated successfully",
        },
        status=200,
    )


"""
curl -X POST \
--data '{"status": "done"}' \
http://127.0.0.1:8001/api/update-todo/
"""
