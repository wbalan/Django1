from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import journal
from .models import journ_bat
from .models import car
from .models import battery
from datetime import timedelta
from .forms import UchetAddForm

def journal_list(request):
    jour_list = journal.objects.all().order_by("-date_purch")
    return render(request, "journal.html", {"jour_list": jour_list})

def journal_add(request):
    if request.method == "POST":
        pass


    else:
        userform = UchetAddForm()
        jrn = journal.objects.get(pk=48)
        userform = UchetAddForm(instance=jrn)
        userform.fields['malf'].label = "....."
        userform.initial['malf']='Оборудование исправно'
        return render(request, "journ_add.html",  {"form": userform})

def journal_create(request):
    print(request.method)
    if request.method == "POST":
        jrn = journal()
        jrn.date_purch = request.POST.get('date')
        jrn.acc = request.POST.get('acc')
        jrn.number = request.POST.get('acc')
        jrn.malf = request.POST.get('malf')
        jrn.work_hours = request.POST.get('work_hours')+":"+request.POST.get('work_minutes')
        if request.POST.get('date_rep')!="":
            jrn.date_rep = request.POST.get('date_rep')
        else:
            jrn.date_rep = None
        jrn.save()
        return HttpResponseRedirect("/uchet")

def journal_add1(request):
    return render(request, "journ_add.html")

def journal_edit(request, number):
    try:
        jrn_ed = journal.objects.get(id=number)
        print(jrn_ed.malf)
        if request.method == "POST":
            jrn = journal()
            jrn.id = number
            jrn.date_purch = request.POST.get('date')
            jrn.acc = request.POST.get('acc')
            jrn.number = request.POST.get('acc')
            jrn.malf = request.POST.get('malf')
            jrn.work_hours = request.POST.get('work_hours') + ":" + request.POST.get('work_minutes')
            if request.POST.get('date_rep') != "":
                jrn.date_rep = request.POST.get('date_rep')
            else:
                jrn.date_rep = None
            jrn.save()
            return HttpResponseRedirect("/uchet")
        else:
            d = str(jrn_ed.malf)
            #d = d.split()
            a= jrn_ed.work_hours.split(":")
            return render(request, "journal_edit.html", {"jrn_ed": jrn_ed, "a": a[0], "b": a[1], "d": "<h2>это просто пиздец</h2>"})
    except journal.DoesNotExist:
        return HttpResponseNotFound("<h2>Запись не найдена</h2>")
def journal_delete(request, number):
    try:
        jrn=journal.objects.get(id=number)
        jrn.delete()
        return HttpResponseRedirect("/uchet")
    except:
        return HttpResponseNotFound("<h2>Запись не найдена</h2>")



# Create your views here.

