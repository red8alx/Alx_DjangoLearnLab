from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')
    def __str__(self):
        return f"{self.title} by {self.author}" 
    #Extending Book Model with Custom Permissions
    class Meta(models.Model):
        Permissions_Choices =(
            ('can_add_book', 'can_add_book'),
            ('can_change_book', 'can_change_book'),
            ('can_delete_book', 'can_delete_book'),

        )
    permissions = models.CharField(max_length=50,  choices='Permissions_Choices')
    meta = models.TextField()
    
    def __str__(self):
        return f'{self.user.username} - {self.permissions}'

class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name='books')
    def __str__(self):
        return self.name 
class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='library')
    def __str__(self):
        return self.name
#Extending User Model with a UserProfile
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    Role_Choices =(
        ('Admin','Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    
    )

role = models.CharField(max_length=50,  choices='Role_Choices')
userprofile = models.TextField()

def __str__(self):
    return f'{self.user.username} - {self.role}'

#Signal to automatically create a UserProfile when a new User is created
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()



class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        
        #Validating Email
        if not email:
            raise ValueError('User must have an email address')
        #Fetching and normalizing email
        user = self.model(email=self.normalize_email(email), **extra_fields)

        #Setting password (hashes password)
        user.set_password(password)
        #saving created user in current database
        user.save(using=self._db)
        #returning created user
        return user
    
    #creating superuser ensuring administrative users can be created with the required fields fields
    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
#Custom User Model by extending AbstractUser
#from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(default='2020-01-01', blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile_photos', blank=True, null=True)

    objects = CustomUserManager()
    def __str__(self):
        return self.email