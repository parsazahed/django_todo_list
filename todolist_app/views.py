from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist_app.models import Task
from todolist_app.forms import Taskform
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    context = {
        'index_text':"Welcome to Index Page",
        }
    return render(request, "index.html", context)

def todolist(request):

    #########################   New Task Form   #########################
    if request.method == "POST":
        form = Taskform(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,"your task has been added!")
        return redirect('todolist')
    else:
        all_tasks = Task.objects.all()
        paginator = Paginator(all_tasks,5)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        return render(request, "todolist.html", {"all_tasks":all_tasks})

def delete_task(request , task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('todolist')

def edit_task(request, task_id):
    if request.method == "POST":
        task = Task.objects.get(pk=task_id)
        form = Taskform(request.POST or None, instance=task)
        if form.is_valid:
            form.save()
        messages.success(request,("Your task has been edited!"))
        return redirect('todolist')
    else:
        task_obj = Task.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj':task_obj})

def complete(request, task_id):
    task = Task.objects.get(pk=task_id)
    if task.done is False:
        task.done = True
        task.save()
        messages.success(request,("Your task has been completed!"))
    else:
        task.done = False
        task.save()
        messages.warning(request,("Your task has not been completed!"))
    return redirect('todolist')


def contact(request):
    context = {
        'contact_text':"Welcome to Contact Page",
    }
    return render(request, "contact.html", context)

def about(request):
    context = {
        'about_text':"Welcome to About Page",
    }
    return render(request, "about.html", context)