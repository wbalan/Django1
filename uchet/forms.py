from django import forms
from .models import journal
from django.forms import NumberInput, IntegerField, CharField, TextInput,Textarea

class UchetAddForm(forms.ModelForm):
    malf = forms.CharField(max_length=10,label="ssdfsd",widget=TextInput(attrs={'size':10}))
    class Meta:
        model = journal
        fields = ('number','date_purch','acc','work_hours','malf','date_rep')
        labels = {'number': "Номер погрузчика" , 'date_purch': "Дата учета", 'malf': "Неисправность"}
        widgets ={
            'number': NumberInput(),
            'malf': TextInput(attrs={ 'pattern': "\d{4,4}"}),
        }