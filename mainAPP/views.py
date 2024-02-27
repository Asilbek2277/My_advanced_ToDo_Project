from django.shortcuts import render, redirect
from django.views import View
from .models import *
from django.contrib.auth import authenticate, login, logout


class Task(View):
    def get(self, request):
        if request.user.is_authenticated:
            context = {
               'tasks': Tasks.objects.filter(user=request.user)
            }
            return render(request, 'index.html', context)
        return redirect('/')

    def post(self, request):
        if request.user.is_authenticated:
            Tasks.objects.create(
                user=request.user,
                title=request.POST['title'],
                description=request.POST['description'],
                status=request.POST['status'],
                deadline=request.POST['deadline']
            )
            return redirect('/tasks/')



def delete_task(request, pk):
    if request.user.is_authenticated:
        if Tasks.objects.get(id=pk).user==request.user:
            Tasks.objects.get(id=pk).delete()
            return redirect('/tasks/')
    return redirect('/')




def Tahrirlash(request, pk):
    if request.user.is_authenticated:
        if request.method=='POST':
            element=Tasks.objects.get(id=pk)
            if element.user==request.user:
                element.title=request.POST['title']
                element.description=request.POST['des']
                element.status=request.POST['status']
                element.deadline=request.POST['deadline']
                element.save()

                return redirect('/tasks/')
            return redirect('/')

        context={

            'tasks': Tasks.objects.get(id=pk)
        }

        return render(request, 'edit.html', context)
    return redirect('/')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        user= authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is not None:
            login(request, user)
            return redirect('/tasks/')
        return redirect('/')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')





