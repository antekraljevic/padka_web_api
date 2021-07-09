from django.db import models  
class Transitions(models.Model):  
    id = models.AutoField(primary_key=True)
    priority = models.DecimalField(max_digits=5, decimal_places=4)
    name = models.CharField(max_length=200)
    filename = models.FileField(upload_to='assets/transitions/files')
    thumbnail = models.FileField(upload_to='assets/transitions/thumbnail')
    class Meta:  
        db_table = "transitions"