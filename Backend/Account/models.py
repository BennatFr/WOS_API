from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import PermissionsMixin

# Manager personnalisé pour le modèle utilisateur
class CustomUserManager(BaseUserManager):
    def create_user(self, email, language, password=None):
        if not email:
            raise ValueError('Les utilisateurs doivent avoir une adresse email')
        if not language:
            raise ValueError('Les utilisateurs doivent définir une langue')

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            language=language
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, language, password=None):
        user = self.create_user(
            email=email,
            language=language,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# Modèle CustomUser
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    language = models.CharField(max_length=2, default='US')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['language']

    def __str__(self):
        return self.email