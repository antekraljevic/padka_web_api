from django.db import models
class Transitions(models.Model):  
    id = models.AutoField(primary_key=True)
    priority = models.DecimalField(max_digits=5, decimal_places=4)
    name = models.CharField(max_length=200)
    filename = models.FileField(upload_to='assets/transitions/files')
    thumbnail = models.FileField(upload_to='assets/transitions/thumbnail')
    class Meta:  
        db_table = "transitions"

class Reactions(models.Model):
    id = models.AutoField(primary_key=True)
    priority = models.DecimalField(max_digits=5, decimal_places=4)
    name = models.CharField(max_length=200)
    filename = models.FileField(upload_to='assets/reactions/files')
    thumbnail = models.FileField(upload_to='assets/reactions/thumbnail')
    class Meta:  
        db_table = "reactions"

class Music(models.Model):
    def get_filename_path(instance, filename):
        return 'assetss/music/{0}/files/{0}/{1}'.format(instance.type, filename)
        
    def get_thumbnail_path(instance, filename):
        return 'assets/music/thumbnail/{0}/{1}'.format(instance.type, filename)

    id = models.AutoField(primary_key=True)
    priority = models.DecimalField(max_digits=5, decimal_places=4)
    name = models.CharField(max_length=200)
    filename = models.FileField(upload_to=get_filename_path)
    thumbnail = models.FileField(upload_to=get_thumbnail_path)
    type = models.CharField(max_length=200)
    class Meta:  
        db_table = "music"