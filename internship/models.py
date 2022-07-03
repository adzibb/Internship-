from random import choices
from unicodedata import name
from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    interns_letter = models.FileField()
    # date of application

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=200)
    about = models.TextField()
    # date_posted = the day posted
    # date_due = the number of days left

    def __str__(self):
        return self.name
    

class Location(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    digi_address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class CompanyRole(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    addi_info = models.CharField(max_length=400, null=True)

    def __str__(self):
        return self.name

# class Department(models.Model):
#     depart = (
#         ('CS', 'Computer Sciene'),
#         ('ES', 'Environmental Sciene'), 
#         ('BC', 'Biochemistry'),
#     )
#     role = models.ForeignKey(CompanyRole, on_delete=models.CASCADE)
#     name = models.CharField(max_length=3, choices=depart)

#     def __str__(self):
#         return self.name


# class CompanyRequired(models.Model):
#     role = models.ForeignKey(CompanyRole, on_delete=models.CASCADE)




