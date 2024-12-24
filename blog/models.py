from django.db import models


class Task(models.Model):
    title = models.CharField("Название задачи", max_length=200)
    task = models.TextField("Описание задачи")

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def _str_(self):
        return self.title

