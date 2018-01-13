from django.db import models

# Create your models here.


class Entity(models.Model):
    name = models.CharField(max_length=200)
    liked = models.IntegerField
    type = models.CharField(max_length=200)


class Incident(models.Model):
    date = models.DateField('date of incident')
    involved = models.ForeignKey(Entity, on_delete=models.CASCADE)
    liked = models.IntegerField


class FixedResponse(models.Model):
    intent = models.CharField(max_length=200)
    response = models.CharField(max_length=200)

