from django.db import models

class Operation(models.Model):

    name = models.TextField(
        verbose_name = "Наименование операции",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание операции",
    )
    cost = models.FloatField(
        verbose_name="Стоимость",
    )
    class Meta:
        verbose_name = "Операция"
        verbose_name_plural = "Операции"
    
    def __str__(self):
        return f"{self.name}"
