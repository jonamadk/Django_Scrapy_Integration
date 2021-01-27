from django.db import models

# Create your models here.

class LiveTradingData(models.Model):

    # date_value = models.DateField(auto_now_add=True)
    company_name_symbol = models.CharField(max_length= 20, null = True)
    high_value = models.FloatField(blank= True, null= True)
    low_value = models.FloatField(blank = True, null= True)
    open_value = models.FloatField(blank= True, null = True)
    qty = models.FloatField(blank = True, null = True)
    change_percent_value = models.FloatField(blank = True, null = True)

    # class Meta:
    #     verbose_name= "Live Trading Data"
    
    # def __str__(self):
    #     return self.date_value









    