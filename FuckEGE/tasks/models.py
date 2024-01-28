from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Task(models.Model):
    task_num = models.IntegerField(unique=True, verbose_name="Номер задания",
                                   validators=[MinValueValidator(1),
                                               MaxValueValidator(27)
                                               ])
    answer = models.TextField(verbose_name="Ответ")

    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"
        ordering = ['task_num']

    def __str__(self):
        return f"Задание {self.task_num}"


class Message(models.Model):
    time_and_date = models.DateTimeField(auto_now_add=True,
                                         verbose_name="Время отправки")
    text = models.CharField(max_length=100, verbose_name="Сообщение")

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

    def __str__(self):
        return self.text
