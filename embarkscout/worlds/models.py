from django.db import models

# Create your models here.
class WorldGenParams(models.Model):
    df_version = models.CharField(max_length=20, default='0.40.24')
    name = models.CharField(max_length=20)
    params = models.TextField()
    
    def __str__(self):
        return self.name

class World(models.Model):
    df_version = models.CharField(max_length=20)
    world_gen_params = models.ForeignKey(WorldGenParams)
    es_version = models.IntegerField(null=True)
    name = models.CharField(max_length=50,null=True)
    name_english = models.CharField(max_length=80,null=True)
    width = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    year = models.IntegerField(null=True)

    seed = models.CharField(max_length=30,null=True)
    history_seed = models.CharField(max_length=30,null=True)
    name_seed = models.CharField(max_length=30,null=True)
    creature_seed = models.CharField(max_length=30,null=True)

    def __str__(self):
        if (self.name == None):
            return "Incomplete " + self.world_gen_params.name
        else:
            return self.name + " \"" + self.name_english + "\" (" + self.world_gen_params.name + ")"