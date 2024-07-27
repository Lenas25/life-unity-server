from django.db import models
from authentication.models import UserModel


# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=255, null=False, blank=True)
    content = models.TextField(null=False, blank=True)
    color = models.CharField(max_length=255, null=False, blank=True)
    emojis = models.TextField(null=False, blank=True)

    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True, related_name='user_id')

    class Meta:
        db_table = 'notes'

    def __str__(self):
        return self.title
