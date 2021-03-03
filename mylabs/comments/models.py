from django.db import models

# Create your models here.

class ServMonitor(models.Model):
    name = models.CharField("Имя", max_length=150)
    time = models.TimeField()
    type = models.CharField("Тип оповещения", max_length=150)
    email = models.EmailField()
    group = models.CharField("Группа серверов", max_length=150)
    group_type = models.CharField("Тип группы серверов", max_length=150)
    gps = models.GenericIPAddressField()
    url = models.SlugField(max_length=160, unique=True, null=False)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.name

    '''class Meta:
        verbose_name = "Имя"
        verbose_name_plural = "Имя"'''
