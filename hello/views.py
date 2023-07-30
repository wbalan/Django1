from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Car
from .models import Card
from .models import RouteSheet


def index(request):
    car = Car.objects.all()
    return render(request, "index.html", {"car": car})

#сохранение данных в БД
def create(request):
    if request.method == "POST":
        card = Card()
        card.type = request.POST.get("type")
        card.inn = request.POST.get("inn")
        card.sn = request.POST.get("sn")
        card.gs = request.POST.get("gs")
        card.dateofpurchase = request.POST.get("dateofpurchase")
        card.dateofpurchaseakb = request.POST.get("dateofpurchaseakb")
        card.gsakb = request.POST.get("gsakb")
        card.snakb = request.POST.get("snakb")
        card.save()
        return HttpResponseRedirect("/")

#изменение данных в БД
def edit(request, number):
    try:
        card = Card.objects.get(inn = number)

        if request.method == "POST":
            card.type = request.POST.get("type")
            card.inn =request.POST.get("inn")
            card.sn = request.POST.get("sn")
            card.snakb = request.POST.get("snakb")
            card.gsakb = request.POST.get("gsakb")
            card.gs = request.POST.get("gs")
            card.dateofpurchase = request.POST.get("dateofpurchase")
            card.dateofpurchaseakb = request.POST.get("dateofpurchaseakb")
            card.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"card":card})
    except Card.DoesNotExist:
        return HttpResponseNotFound("<h2>Погрузчик не найден</h2>")

#удаление данных из базы
def delete(request, number):
    try:
        car = Car.objects.get(number=number)
        car.delete()
        return HttpResponseRedirect("/")
    except Car.DoesNotExist:
        return HttpResponseNotFound("<h2>Car not found</h2>")

def list(request):
    card = Card.objects.all()
    return render(request, "list.html", { "card" : card})

def add(request):
    card = Card.objects.all()
    return render(request, "add.html", { "card" : card})

def viewroute(request):
    route = RouteSheet.objects.all()
    return render(request, "listroute.html", {"route": route})

def createroute(request):
    if request.method == "POST":
        jrn = journal.objects.all()
        jrn_bat = journ_bat.ojects.all()
        route.kindofoperation = request.POST.get("kindofoperation")
        route.dateoperation = request.POST.get("dateoperation")
        route.driver = request.POST.get("driver")
        route.stateout = request.POST.get("stateout")
        route.running = request.POST.get("running")
        route.card_id = request.POST.get("card")
        route.charge = request.POST.get("charge")
        route.save()
        return HttpResponseRedirect("/listroute/")
    card = Card.objects.all()
    return render(request, "createroutelist.html",{"card": card })