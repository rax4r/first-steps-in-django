from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms

tasks = []
class NewTasksForm(forms.Form):
    task = forms.CharField(label="New task")
# Create your views here.

def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })
def add(request):
    if request.method== "POST":
        form = NewTasksForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"] 
            tasks.append(task)
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html",{
                "form": form
            })
    return render(request, "tasks/add.html",{
        "form": NewTasksForm()
    })