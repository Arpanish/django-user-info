from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.contrib.auth.models import UserManager
# Create your models here.
class User(AbstractUser):
    full_name = models.CharField(max_length=55)
    email = models.EmailField(max_length=55,unique=True)
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phone_number = models.CharField(validators = [phoneNumberRegex], max_length = 16,unique=True)
    address = models.CharField(max_length=20)
    is_superuser = models.BooleanField('is superuser',default = False)
    is_staff = models.BooleanField('is staff',default=False)
    username = models.CharField(max_length=15,unique=True,error_messages={'required': 'Enter a valid phone number',
                         'invalid': 'Enter a valid phone number'})
    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = []
    objects = UserManager()



# user docs model
class UserDoc(models.Model):
       bbox = models.CharField(max_length=15)
       docs_image_url = models.ImageField()
       doc_type = models.CharField(max_length=55)
       user = models.ForeignKey('User', on_delete=models.CASCADE)

