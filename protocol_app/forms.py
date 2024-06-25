import re
from .models import *
from django import forms
from django.core.exceptions import ValidationError


class LoginUserForm(forms.Form):

    username = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'placeholder': 'Логин', 'class': 'login--input'}))
    password = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'placeholder': 'Пароль', 'class': 'login--input'}))


class CreateEmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('full_name', 'date_check', 'name_chairman', 'previous_date_eb_time',
                  'post_chairman', 'name_first_member_commission',
                  'post_first_member_commission', 'name_second_member_commission',
                  'post_second_member_commission', 'responsible_electrical_industry',
                  'work_experience', 'reason', 'previous_date_eb',
                  'fire_safety_instruction', 'special')

    date_check = forms.DateField(label='Дата проверки знаний', widget=forms.DateInput(attrs={'type': 'date'}))
    previous_date_eb_time = forms.DateField(label='Предыдущая дата ЭБ', widget=forms.DateInput(attrs={'type': 'date'}))

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        # Регулярное выражение для поиска цифр и специальных символов
        if re.search(r'[\d!@#$%^&*()_+=\[\]{};:"\\|,.<>/?]', full_name):
            raise ValidationError("ФИО не должно содержать цифр и специальных символов")
        return full_name

    def clean_name_chairman(self):
        name_chairman = self.cleaned_data.get('name_chairman')
        if re.search(r'[\d!@#$%^&*()_+=\[\]{};:"\\|,.<>/?]', name_chairman):
            raise ValidationError("ФИО не должно содержать цифр и специальных символов")
        return name_chairman

    def clean_name_first_member_commission(self):
        name_first_member_commission = self.cleaned_data.get('name_first_member_commission')
        if re.search(r'[\d!@#$%^&*()_+=\[\]{};:"\\|,.<>/?]', name_first_member_commission):
            raise ValidationError("ФИО не должно содержать цифр и специальных символов")
        return name_first_member_commission

    def clean_name_second_member_commission(self):
        name_second_member_commission = self.cleaned_data.get('name_second_member_commission')
        if re.search(r'[\d!@#$%^&*()_+=\[\]{};:"\\|,.<>/?]', name_second_member_commission):
            raise ValidationError("ФИО не должно содержать цифр и специальных символов")
        return name_second_member_commission

    def clean_work_experience(self):
        work_experience = self.cleaned_data.get('work_experience')
        # Регулярное выражение для поиска цифр и специальных символов
        if any(char == '-' or char == '+' for char in str(work_experience)):
            raise ValidationError("Стаж работы должен содержать только цифры")
        return work_experience
