from django.db import models

# Create your models here.
class Car(models.Model):
    number = models.PositiveSmallIntegerField(unique=True,verbose_name='Номер')
    description = models.TextField()

class Card(models.Model):
    type=models.CharField(unique=False, verbose_name='Тип погрузчика', max_length=25)
    inn=models.PositiveSmallIntegerField(unique=True, verbose_name='Инвентарный номер')
    sn=models.CharField(unique=True, verbose_name="Заводской номер", max_length=15)
    dateofpurchase = models.DateField(verbose_name="Дата приобретения")
    dateofpurchaseakb = models.DateField(verbose_name="Дата приобретения")
    snakb = models.CharField(unique=True, verbose_name="Серийный номер АКБ", max_length=15)
    gsakb=models.DateField(verbose_name="Гарантия АКБ до")

class RouteSheet(models.Model):
    card = models.ForeignKey( "Card", on_delete=models.CASCADE, null=True )
    kindofoperation = models.CharField(verbose_name="Вид операции", max_length=20, null=True)
    dateoperation = models.DateTimeField(verbose_name="Дата операции", null=True)
    driver = models.CharField(null=True, max_length=20, default="ww")
    stateout = models.CharField(verbose_name="Неисправности", max_length=20, null=True)
    running = models.SmallIntegerField(verbose_name="Наработка", null=True)
    charge = models.CharField(verbose_name="Зарядка", max_length=20, null=True)
