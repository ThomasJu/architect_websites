from django.db import models

# Create your models here.
# four attributes name/ title / experience / picture
class Employee(models.Model):
    name = models.CharField(max_length=100, help_text='Enter the name of Employee')
    title = models.CharField(max_length=100, help_text='Enter the title of Employee')
    experience = models.TextField(max_length=1000, help_text="Enter the working experience of Employee")
    picture = models.ImageField(upload_to='images/employees_picture')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name
    
# four attributes name / location / intro /pictures
class Case(models.Model):
    name = models.CharField(max_length=100, help_text='Enter the name of the case')
    location = models.CharField(max_length=100, help_text='Enter the location of the case')
    intro = models.TextField(max_length=1000, help_text="Enter a brief introduction of this case")
    pictures = models.ManyToManyField('Image')
    
    def __str__(self):
        return self.name

# used for adding many pictures in case
class Image(models.Model):
    picture = models.ImageField(upload_to='images/cases_picture')