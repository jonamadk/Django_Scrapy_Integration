from django.db import models

# Create your models here.

class Data(models.Model):

    title = models.TextField(null = True,blank=True)


# item = Data(title=item.get())




    