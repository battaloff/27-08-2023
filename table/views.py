from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import JsonResponse

from .models import Tasks


# rendering home page
def home(request):
    task_list = Tasks.objects.all()
    context = {"task_list": task_list}
    return render(request, 'base.html', context)


def update_task_status(request):
    if request.method == "POST":
        task_id = request.POST.get("task_id")
        status = request.POST.get("status")

        # Update the task status in the database
        task = Tasks.objects.get(id=task_id)
        task.status = status
        task.save()

        # Return a JSON response indicating success
        return JsonResponse({"status": "success"})

    # Return a JSON response indicating an error if the request method is not POST
    return JsonResponse({"status": "error", "message": "Invalid request method"})


