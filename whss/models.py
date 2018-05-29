from django.db import models
# from datetime import datetime


# default=datetime.now, blank=True, null=True
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    # class Meta:
        # verbose_name_plural = "Users"
