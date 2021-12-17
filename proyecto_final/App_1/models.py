from django.db import models
 

class Internos(models.Model):

    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    trabajo=models.CharField(max_length=40)
    horas_de_trabajo = models.IntegerField() 


class jefes_de_trabajo(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    trabajo= models.CharField(max_length=30)
    email= models.EmailField()
    

class maestros(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    materia= models.CharField(max_length=30)
    email= models.EmailField()

class preceptores(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

    
