from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    subsystem = models.CharField(max_length=200)
    
class SensorLog(models.Model):
    name = models.ForeignKey('Sensor', models.DO_NOTHING, db_column='name')
    value = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)
    
class Actuator(models.Model):
    name = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    subsystem = models.CharField(max_length=200)

class ActuatorLog(models.Model):
    name = models.ForeignKey('Actuator', models.DO_NOTHING, db_column='name')
    state = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)