from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.admin import UserAdmin
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    class Meta:
        permissions = [
            ("can_add_book", "can_add_book"),
            ("can_change_book", "can_change_book"),
            ("can_delete_book", "can_delete_book"),
        ]
    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book)
    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=255)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member')
    ]
    role = models.CharField(max_length=255, choices=ROLE_CHOICES)

def create_user_profile(instance):
    UserProfile.objects.create(user=instance)

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("You did not enter a valid email address.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()

class ModelAdmin(UserAdmin):
    ordering = ('date_of_birth', 'profile_photo')
