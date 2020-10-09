from django.db import models
from django.contrib.auth.models import User



class Expense(models.Model):
    amount=models.FloatField(default=0.00)
    date=models.DateTimeField(auto_now_add=True)
    description=models.TextField()
    owner=models.ForeignKey(to=User,on_delete=models.CASCADE)
    category=models.CharField(max_length=200)

    def __str__(self):
        return str(self.owner)
        
