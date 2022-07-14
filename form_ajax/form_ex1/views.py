import re
from statistics import mode
from turtle import title
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
import faker
from . import forms
from . import models

# Create your views here.

def home(request):
    form = forms.DataLoginForm(request.POST or None, request.FILES or None)
    data = {}
    if request.method == "POST":
        if form.is_valid():
            form.save()
            data["login"] = form.cleaned_data.get("login")
            data["password"] = form.cleaned_data.get("password")
            data["password_conf"] = form.cleaned_data.get("password_conf")
            data["birth_date"] = form.cleaned_data.get("birth_date")
            data["status"] = "ok"
            print(data)
            return JsonResponse(data)
        else:
            errors = [e[0].message for e in form.errors.as_data().values()]
            return JsonResponse({"status": "error", "mes" : errors})
    print("here")
    context = {"form" : form}
    return render(request, "form_ex1/base.html", context)


def generate_data(request):
    print("generating")
    f = faker.Faker()
    for t in f.words(100):
        models.Movie.objects.create(title=t)
    return JsonResponse({"status" : "ok", "mes" : "movies created"})


def autocomplete(request):
    
    print(request, "!!!!!!!!!!!!!!")
    if request.method == "POST":
        form = forms.MovieForm(request.POST or None, request.FILES or None)
        form.save()
        m = form.cleaned_data.get("title")
        qs = models.Movie.objects.filter(title__istartswith=m)
        titles = [m.title for m in qs]
        titles = list(set(titles))
        titles.remove(m)
        print(qs)
        return JsonResponse({"status" : "ok", "titles" : titles})
    print("here")
    context = {}
    return render(request, "form_ex1/autocomplete.html", context)
    