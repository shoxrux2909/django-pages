from django.db import models

# Create your models here.
class Talaba(models.Model):
    ism = models.CharField(max_length=150)
    familiya = models.CharField(max_length=150)
    yosh = models.IntegerField()
    sana = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.ism} {self.familiya}"