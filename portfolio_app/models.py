from django.db import models

class Services(models.Model):
    icon = models.ImageField(upload_to='services/icons/')
    title = models.CharField(max_length=250)
    description = models.TextField()


    def __str__(self):
        return self.title

class Projects(models.Model):
    image = models.ImageField(upload_to='media/images/')
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    links = models.URLField(max_length=500 ,blank=True, default=None)

    def __str__(self):
        return self.title

class Tools(models.Model):
    name = models.CharField(max_length=50)