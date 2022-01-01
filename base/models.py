from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Question(models.Model):
    opt1 = CharField(max_length=200)
    opt2 = CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    img1 = CharField(max_length=2048)
    img2 = CharField(max_length=2048)
    # votes1  (Incremental Count)
    # votes2  (Incremental Count)
    # Yet we have to save vote object to note if user already voted

    class Meta:
        # -updated vs updated => ascending order vs descending order
        ordering = ['-updated', '-created']
    def __str__(self):
        return self.opt1 + ' or ' + self.opt2