from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    price = models.CharField(max_length=200)
    color = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    manager = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.name

class Contacts(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    message = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class appointment(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    date = models.DateField()
    department = models.CharField(max_length=50)
    doctor = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name

class Members(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=50)




class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=50)


    def __str__(self):
        return self.title


class Admin(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Admin(models.Model):

    username = models.CharField(max_length=200)
    password = models.CharField(max_length=50)












