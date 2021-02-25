from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, full_name , password=None):
        if not email:
            raise ValueError('users must have Email')
        if not full_name:
            raise ValueError('users must have Full Name')
        
        user = self.model(email = self.normalize_email(email), full_name=full_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email , full_name , password=None):
        user = self.create_user(email , full_name , password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user 