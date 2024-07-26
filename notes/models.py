from django.db import models

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    color = models.CharField(max_length=255, null=False, blank=False)
    emojis = models.TextField(null=False, blank=False)

    class Meta:
        db_table = 'notes'

    def __str__(self):
        return self.title
