from django.db import models
from apps.account.models import Account


class Contact(models.Model):
    user = models.ForeignKey(Account ,on_delete=models.CASCADE)
    title = models.CharField(max_length=65)
    phone_number = models.CharField(max_length=12)
    from_here = models.CharField(max_length=50) 
    to_here = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)

    def str(self):
        return self.title
    