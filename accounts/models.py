from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager

class User(AbstractBaseUser):
    email = models.EmailField(max_length=100, unique = True)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default = True)
    is_admin = models.BooleanField(default = False)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.email
    
    def has_perm(self, perm , obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin
    
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.FileField(blank=True, null=True, upload_to='avatar/')

    def __str__(self):
        return self.user.email