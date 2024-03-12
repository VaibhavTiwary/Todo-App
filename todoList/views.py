from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Todo
from django.template import loader

def index(request):
    all_list = Todo.objects.all
    if request.method == "POST":
        items = request.POST["input"]
        data = Todo(item = items)
        data.save()
    
    return render(request, "todoList/index.html", {"all_list":all_list})
    
    

def delete(request, id):
    member = Todo.objects.get(id = id)
    member.delete()
    return HttpResponseRedirect(reverse('todo:index'))

def update(request, id):
    member = Todo.objects.get(id = id)
    # template = loader.get_template("update.html")
    context = {
        "mymember": member,
    }
    return render(request, "todoList/update.html", context)

def updaterecord(request, id):
    items = request.POST["input"]
    member = Todo.objects.get(id = id)
    member.item = items
    member.save()
    return HttpResponseRedirect(reverse('todo:index'))