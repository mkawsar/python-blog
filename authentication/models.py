from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    phone = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='created_by_id', on_delete=models.DO_NOTHING, null=True,
                                   blank=True)
    update_by = models.ForeignKey(User, related_name='updated_by_id', on_delete=models.DO_NOTHING, null=True,
                                  blank=True)

    class Meta:
        db_table = 'users_details'
