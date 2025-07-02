from django.db import models
from django.contrib.auth.models import AbstractUser

from accaunts.models import RoleChoice


class DeleteModel(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True )
    updated_at = models.DateTimeField(auto_now_add=True, blank = True, null= True)
    is_deleted = models.BooleanField(default=False)

    objects = DeleteModel()
    new = models.Manager()

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        self.is_deleted=True
        self.save(*args, **kwargs)


class CustomUser(AbstractUser):
    role = models.CharField(default=RoleChoice.READER, choices=RoleChoice, max_length=20)
    phone_num=models.CharField(max_length=100)

class Avtor(BaseModel):
    role = models.CharField(default=RoleChoice.READER, choices=RoleChoice, max_length=20)
    name = models.CharField(models.Model)



class Books(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField()
    isbn = models.CharField(max_length=200)
    price = models.IntegerField()
    # avtor = models.ForeignKey(Avtor, on_delete=models.CASCADE)
    # photo = models.ImageField(upload_to='books/')
    # file = models.FileField(upload_to='documents/')







