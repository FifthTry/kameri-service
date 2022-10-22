import django.http
from django.core.exceptions import ObjectDoesNotExist
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Todo
from .forms import AddTodoForm


@csrf_exempt
def apis(req: django.http.HttpRequest):
    from django.shortcuts import render
    return render(req, "index.html")


@csrf_exempt
def add_todo(req: django.http.HttpRequest):

    if not req.tid:
        return django.http.HttpResponse("tid is required")

    if req.method != "POST":
        return django.http.HttpResponse(
            "wrong method: only POST allowed, got: %s" % req.method, status=405
        )

    # TODO: in future we will allow `form = AddTodoForm(ftd_django.get_data(req))`.
    #       `.get_data()` will look for both json data if content-type is application/json,
    #       and form data if content-type is application/x-www-form-urlencoded.
    form = AddTodoForm(json.loads(req.body.decode("utf-8")))

    if not form.is_valid():
        # TODO: with helper this would look like: `return ftd_django.form_error(form)`
        # Note: we are returning status 200 because if we return say 400, browser
        #       will show a popup saying "Failed to load resource". This is not
        #       what we want.
        return django.http.JsonResponse({"errors": form.errors})

    Todo.objects.create(
        title=form.cleaned_data["title"],
        status=form.cleaned_data["status"],
        description=form.cleaned_data["description"],
        tracker=req.tid,
    )

    # TODO: url should be constructed using `mount-point` header if present
    #       in future we can provide a helper so we can write:
    #       `return ftd_django.redirect("/", req)`
    return django.http.JsonResponse({"redirect": "/"})


"""
curl -X POST \
--data '{"title": "Take update from Interns"}' \
http://127.0.0.1:8001/api/add-todo/
"""

"""
curl -X POST \
--data '{"title": "Take update from Interns", "status": "In Progress", "description": "Description"}' \
https://kameri-service.herokuapp.com/api/add-todo/
"""


def list_todo(req: django.http.HttpRequest):

    if not req.tid:
        return django.http.HttpResponse("tid is required")

    return django.http.JsonResponse(
        [
            {
                "id": x.id,
                "title": x.title,
                "status": x.status,
                "description": x.description,
            }
            for x in Todo.objects.filter(tracker=req.tid).order_by("-updated_at")
        ],
        safe=False,
    )


"""
curl -X GET http://127.0.0.1:8001/api/todos/
"""

"""
curl -X GET https://kameri-service.herokuapp.com/api/todos/
"""


@csrf_exempt
def update_todo(req: django.http.HttpRequest):

    if not req.tid:
        return django.http.HttpResponse("tid is required")

    if req.method != "POST":
        return django.http.HttpResponse("Wrong Method", status=405)

    body = json.loads(req.body.decode("utf-8"))
    id = body.get("id")
    status = body.get("status")

    if not status:  # TODO:
        return django.http.JsonResponse(
            {
                "error": {"todo#status": "Status is mandatory field"},
                "message": "missing mandatory fields",
            },
            status=200,
        )

    if not id:  # TODO:
        return django.http.JsonResponse(
            {
                "error": {"todo#status": "Status is mandatory field"},
                "message": "missing mandatory fields",
            },
            status=200,
        )

    try:
        todo = Todo.objects.get(id=id)
    except ObjectDoesNotExist:
        raise  # TODO: handle this

    todo.status = status
    todo.save()
    return django.http.JsonResponse({"reload": True})


"""
curl -X POST \
--data '{"id": 1, "status": "done"}' \
http://127.0.0.1:8001/api/update-todo/
"""

"""
curl -X POST \
--data '{"id": 1, "status": "done"}' \
https://kameri-service.herokuapp.com/api/update-todo/
"""
