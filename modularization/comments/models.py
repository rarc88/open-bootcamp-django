from django.db import models


class Comment(models.Model):

    name = models.CharField(max_length=255, null=False)
    score = models.IntegerField(default=3)
    comment = models.TextField(max_length=1000, null=True)
    date = models.DateField(null=True)

    def __str__(self) -> str:
        return self.name
