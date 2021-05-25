from django.db import models

# Create your models here.



from django.db import models


from django.db.models import Model


class Blog(Model):
    name = models.CharField(max_length=128)
    user = models.ForeignKey( 'auth.User'  ,on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    
