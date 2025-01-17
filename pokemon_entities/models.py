from django.db import models 

class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon= models.ForeignKey(
        Pokemon,
        on_delete=models.deletion.CASCADE
    )
    lat = models.FloatField()
    lon = models.FloatField()
