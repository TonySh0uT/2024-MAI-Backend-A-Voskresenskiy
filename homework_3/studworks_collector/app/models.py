from django.db import models


class Student(models.Model):
    uid = models.UUIDField(verbose_name='ID студента', primary_key=True)
    first_name = models.CharField(max_length=255, verbose_name='Имя студента', blank=False)
    last_name = models.CharField(max_length=256, verbose_name='Фамилия студента', blank=False)


class Adviser(models.Model):
    uid = models.UUIDField(verbose_name='ID руководителя', primary_key=True)
    first_name = models.CharField(max_length=256, verbose_name='Имя руководителя', blank=False)
    last_name = models.CharField(max_length=256, verbose_name='Фамилия руководителя', blank=False)


class CourseWork(models.Model):
    uid = models.UUIDField(verbose_name='ID курса', primary_key=True)
    name = models.CharField(max_length=256, verbose_name='Тема курсовой работы', blank=False)
    description = models.TextField(verbose_name='Описание курсовой работы')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Исполнитель', blank=False)
    adviser = models.ForeignKey(Adviser, on_delete=models.CASCADE, verbose_name='Руководитель', blank=False)

    def __str__(self):
        return f'{self.name} [{self.uid}]'

    class Meta:
        verbose_name = "Курсовая работа"
        verbose_name_plural = "Курсовые работы"