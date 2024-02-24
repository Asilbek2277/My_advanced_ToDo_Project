from django.shortcuts import render, redirect
from django.views import View
from .models import *

class Task(View):
    def get(self, request):
        context={
           'tasks': Tasks.objects.all()
        }
        return render(request, 'index.html', context)
    def post(self, request):
        Tasks.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            status=request.POST['status'],
            deadline=request.POST['deadline']
        )
        return redirect('/')
def delete_task(request, pk):
    Tasks.objects.get(id=pk).delete()
    return redirect('/')


def Tahrirlash(request, pk):
    if request.method=='POST':
        element=Tasks.objects.get(id=pk)
        element.title=request.POST['title']
        element.description=request.POST['des']
        element.status=request.POST['status']
        element.deadline=request.POST['deadline']
        element.save()

        return redirect('/')

    context={

        'tasks': Tasks.objects.get(id=pk)
    }
        
    return render(request, 'edit.html', context)
