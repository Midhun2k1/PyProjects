from django.db import models
from django import forms


# Create your models here.


from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class FormSubmission(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    mail_id = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    purpose = models.CharField(max_length=50)
    materials_provided = models.ManyToManyField(Material)








# class School(models.Model):
#     name1 = models.CharField(max_length=250)
#
#     def __str__(self):
#         return self.name1
#
#
# class StudentForm(models.Model):
#     GENDER_CHOICES = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#         ('O', 'Other'),
#     )
#
#     DEPARTMENT_CHOICES = (
#         ('commerce', 'Commerce'),
#         ('science', 'Science'),
#         ('arts', 'Arts'),
#     )
#     PURPOSE_CHOICES = (
#         ('place', 'place'),
#         ('order', 'order'),
#         ('return', 'return'),
#     )
#     name = models.CharField(label='Name', max_length=100)
#     dob = models.DateField(label='DOB')
#     age = models.IntegerField(label='Age')
#     gender = models.ChoiceField(label='Gender', choices=GENDER_CHOICES, widget=forms.RadioSelect)
#     phone_number = models.CharField(label='Phone Number', max_length=15)
#     mail_id = models.EmailField(label='Mail ID')
#     address = models.CharField(label='Address', widget=forms.Textarea)
#     department = models.ChoiceField(label='Department', choices=DEPARTMENT_CHOICES)
#     course = models.ChoiceField(label='Course', choices=(), required=False)
#     purpose = models.ChoiceField(label='purpose', choices=PURPOSE_CHOICES)
#     materials = models.TextField()
#
#
#     def __str__(self):
#         return self.name
#
#     def is_valid(self):
#         pass
