from django.db import models

# Create your models here.



from django.db import models


from django.db.models import Model


class Blog(Model):
    name = models.CharField(max_length=128)
    user = models.ForeignKey( 'auth.User'  ,on_delete=models.CASCADE)
    amount = models.FloatField()
    description = models.TextField(blank=True)
    

    def __str__(self):
        return self.name


from django.db import models


from django.db.models import Model


class Comment(Model):
    user = models.ForeignKey( 'auth.User'  ,on_delete=models.CASCADE)
    blog = models.ForeignKey( Blog  ,on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField(blank=True)
    
