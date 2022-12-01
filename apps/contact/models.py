from django.db import models
from apps.account.models import Account
import random


def random_string():
    return str(random.randint(1,10))
    

class CategoryProblem(models.Model):
    title = models.CharField(max_length=50, verbose_name="Nomi")
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Location(models.Model):
    city = mod


class Communication(models.Model):
    CONTACT_STATUS = (
    (0,"Prosess"),
    (1,"Cancelled"),
    (2,"Finished"),
)
    user = models.ForeignKey(Account ,on_delete=models.CASCADE)
    title = models.CharField(max_length=65)
    number_id = models.CharField(max_length=1000,default = random_string,unique=True)    
    image = models.ImageField(null=False, blank=True,verbose_name="Birinchi rasm")
    status = models.IntegerField(choices=CONTACT_STATUS, default=0)
    category = models.ForeignKey(CategoryProblem, on_delete=models.CASCADE, verbose_name="Category")
    lacation = models.CharField(max_length=50)
    description = models.TextField()
    phone_number = models.CharField(max_length=12)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)


    def save(self,request, *args, **kwargs):
        id_number = str(Communication.objects.last.id + 1)
        nols = "0" * (7 - len(id_number)) + id_number
        self.number_id = f"{self.location.city[:1]}" + nols
        return super().save(self, request, *args, **kwargs)

    def str(self):
        return self.title

class CommunicationImage(models.Model):
    communication = models.ForeignKey(Communication, on_delete=models.CASCADE)
    file = models.FileField(upload_to='communications')
    