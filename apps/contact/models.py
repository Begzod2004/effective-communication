from django.db import models
from apps.account.models import Account
import random


def random_string():
    return str(random.randint(10000, 999999))
    

class CategoryProblem(models.Model):
    title = models.CharField(max_length=50, verbose_name="Nomi")
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Communication(models.Model):
    CONTACT_STATUS = (
    (0,"New"),
    (1,"Prosess"),
    (2,"Canceled"),
    (3,"Finished")
)
    user = models.ForeignKey(Account ,on_delete=models.CASCADE)
    title = models.CharField(max_length=65)
    number_problem = models.CharField(max_length=1000,default = random_string)    
    image = models.ImageField(null=False, blank=True,verbose_name="Birinchi rasm")
    status = models.IntegerField(choices=CONTACT_STATUS, default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name="Category")
    lacation = models.CharField(max_length=50)
    description = models.TextField()
    phone_number = models.CharField(max_length=12)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)

    def str(self):
        return self.title
    