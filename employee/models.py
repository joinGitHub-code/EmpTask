from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Task(models.Model):
    employee_name=models.CharField(max_length=25)
    task=models.CharField(max_length=225)     
    time=models.DateTimeField(auto_now=True)#,auto_now_add=True
    comments=models.CharField(max_length=225, blank=True, null=True)

@receiver(post_save,sender=Task)
def saveTask(sender,instance,**kwargs):
    #send_notification(instance)    
    print("Task Saved Successfully")
