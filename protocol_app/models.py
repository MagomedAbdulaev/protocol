from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils import timezone


class Employee(models.Model):
    full_name = models.CharField(max_length=80, verbose_name='ФИО')
    date_check = models.DateField(default=timezone.now, verbose_name='Дата проверки знаний')
    company = models.ForeignKey(to='Company', on_delete=models.CASCADE, verbose_name='Компания')
    name_chairman = models.CharField(max_length=80, verbose_name='ФИО председателя комиссии')
    post_chairman = models.CharField(max_length=80, verbose_name='Должность председателя комиссии')
    name_first_member_commission = models.CharField(max_length=80, verbose_name='ФИО 1-го члена комиссии')
    post_first_member_commission = models.CharField(max_length=80, verbose_name='Должность 1-го члена комиссии')
    name_second_member_commission = models.CharField(max_length=80, verbose_name='ФИО 2-го члена комиссии')
    post_second_member_commission = models.CharField(max_length=80, verbose_name='Должность 2-го члена комиссии')
    responsible_electrical_industry = models.CharField(max_length=80, verbose_name='Ответственный за электрохозяйство')
    work_experience = models.PositiveSmallIntegerField(verbose_name='Стаж работы в годах')
    REASONS = (
        ('Первичная', 'Первичная'),
        ('Повторная', 'Повторная'),
    )
    reason = models.CharField(choices=REASONS, verbose_name='Причина проверки')
    previous_date_eb_time = models.DateField(default=timezone.now, verbose_name='Предыдущая дата ЭБ')
    GROUPS = (
        ('I', 'I'),
        ('II', 'II'),
        ('III', 'III'),
    )
    previous_date_eb = models.CharField(choices=GROUPS, verbose_name='Укажите предыдущую группу по ЭБ')
    BRIEFING = (
        ('Вводный', 'Вводный'),
        ('Первичный на рабочем месте', 'Первичный на рабочем месте'),
        ('Повторный', 'Повторный'),
        ('Внеплановый', 'Внеплановый'),
        ('Целевой', 'Целевой'),
    )
    fire_safety_instruction = models.CharField(choices=BRIEFING, verbose_name='Противопожарный инструктаж')
    special = models.ForeignKey(to='Special', on_delete=models.CASCADE, verbose_name='Специальность')

    def __str__(self):
        return f'{self.full_name}, {self.date_check}'

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'
        ordering = ['full_name', 'date_check']


class Special(models.Model):
    POSTS = (
        ('Водитель', 'Водитель'),
        ('Машинист крана-манипулятора', 'Машинист крана-манипулятора'),
        ('Машинист крана автомобильного', 'Машинист крана автомобильного'),
        ('Машинист  автогидроподъемника', 'Машинист  автогидроподъемника'),
        ('Машинист экскаватора-погрузчика', 'Машинист экскаватора-погрузчика'),
    )
    post = models.CharField(choices=POSTS, verbose_name='Должность')
    number = models.PositiveSmallIntegerField(verbose_name=f'№ Программы ')
    GROUPS = (
        ('I', 'I'),
        ('II', 'II'),
        ('III', 'III'),
    )
    group_eb = models.CharField(choices=GROUPS, default=2, verbose_name='группа ЭБ')
    number_id = models.PositiveBigIntegerField(blank=True, null=True, verbose_name='Номер удостоверения по специальности')

    def __str__(self):
        return f'{self.post}, № Программы {self.number}, группа ЭБ {self.group_eb}'

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'
        ordering = ['post', 'number_id']


class Company(models.Model):
    name = models.CharField(max_length=80, verbose_name='Название')
    specials = models.ManyToManyField(to='Special', verbose_name='Специальности')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
        ordering = ['name', ]


class Person(AbstractUser):
    company = models.ForeignKey(to='Company', on_delete=models.CASCADE, null=True, verbose_name='Компания')

    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username', 'date_joined']
